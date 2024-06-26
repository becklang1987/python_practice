#!/usr/bin/env python3


import json
import locale
import os
import sys
import emails
import reports

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  max_sales={"total_sales":0}
  car_years=[]
  car_year_dict={}
  popular_car_year_sales =0
  popular_car_year =""
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    cy=item['car']['car_year']
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item['total_sales'] > max_sales['total_sales']:
        max_sales=item

    # TODO: also handle most popular car_year
    if cy not in car_years:
        car_years.append(cy)
        car_year_dict[cy]=0
    for kk in car_year_dict.keys():
        if cy == kk :
          car_year_dict[cy] += item['total_sales']



    for year,sales in car_year_dict.items():
        if sales > popular_car_year_sales :
            popular_car_year_sales =sales
            #print(popular_car_year_sales)
            popular_car_year = year




  summary = ["The {} generated the most revenue: ${}".format(format_car(max_revenue["car"]), max_revenue["revenue"]),
            "The car model {} had the most sales: {}.".format(max_sales['car']['car_model'], max_sales['total_sales']),
            "The most popular year was {} with {} sales".format(popular_car_year, popular_car_year_sales)]



  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  print(summary)
  # TODO: turn this into a PDF report
  reports.generate("/tmp/report.pdf", "Summary of Last Month","<br/>".join(summary), cars_dict_to_table(data))

  # TODO: send the PDF report as an email attachment
  emails.sender = "automation@example.com"
  emails.receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  body = "\n".join(summary)

  message = emails.generate(emails.sender, emails.receiver, subject, body, "/tmp/report.pdf")
  emails.send(message)


if __name__ == "__main__":
  main(sys.argv)