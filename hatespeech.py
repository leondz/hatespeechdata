#!/usr/bin/env python3

import scrapy
from html_text import extract_text
import pandas as pd

class HateSpeechSpider(scrapy.Spider):
    name = "hatespeech"

    def start_requests(self):
        yield scrapy.Request(url="https://hatespeechdata.com/")

    def parse(self, response):
        data = []
        dataset_selectors = response.xpath('//h2[@id="list-of-datasets"]/following-sibling::ul')
        title_selectors = response.xpath('//h2[@id="list-of-datasets"]/following-sibling::h4')
        for title, dataset in zip(title_selectors, dataset_selectors):
            row = {}

            title_text = title.css("::text").get()
            row["title"] = title_text

            line_selectors = dataset.css("li").getall()
            if len(line_selectors) == 11:  # other sizes mean its not a dataset table
                for line in line_selectors:
                    text = extract_text(line)
                    field, content = text.split(":", 1)
                    field = "_".join(field.split())
                    row[field] = content

                data.append(row)
    
        df = pd.DataFrame(data)
        df.to_csv("hatespeech.csv", index=False)
    