from typing import Union
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from service import data_clima
from datetime import datetime


data = data_clima(city='Macapá',api_key='6c50c5acf76472ebb2b2f6c47e92087b')
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    time = datetime.now().strftime("%H:%M")
    uv_index = data["uv_index"]
    weather_descriptions = data['weather_descriptions']
    icon = data["icon"]
    temperature = data["temperature"]
    wind_speed = data["wind_speed"]
    humidity = data["humidity"]
    city = f'{data["city"]}-{data["state"]}'
    
    html_content = f"""
    <html>
        <head>
            <title>Weather App</title>
            <!-- Font Awesome -->
            <link
              href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"
              rel="stylesheet"
            />
            
            <!-- Google Fonts -->
            <link
              href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700&display=swap"
              rel="stylesheet"
            />
            
            <!-- MDB -->
            <link
              href="https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/6.4.2/mdb.min.css"
              rel="stylesheet"
            />
        </head>
    <html>
    <body>
        <section class="vh-100" style="background-color: #4B515D;">
            <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-md-8 col-lg-6 col-xl-4">
            <div class="card" style="color: #4B515D; border-radius: 35px;">
              <div class="card-body p-4">
                <div class="d-flex">
                  <h6 class="flex-grow-1">{city}</h6>
                  <h6>{time}</h6>
                </div>

                <div class="d-flex flex-column text-center mt-5 mb-4">
                  <h6 class="display-4 mb-0 font-weight-bold" style="color: #1C2331;">{temperature}c°</h6>
              <span class="small" style="color: #868B94">{weather_descriptions}</span>
                </div>

                <div class="d-flex align-items-center">
                  <div class="flex-grow-1" style="font-size: 1rem;">
                    <div><i class="fas fa-wind fa-fw" style="color: #868B94;"></i> <span class="ms-1"> {wind_speed}km/h
                      </pan></
                    <div><i class="fas fa-tint fa-fw" style="color: #868B94;"></i> <span class="ms-1"> {humidity}% </span>
                    </
                    <div><i class="fas fa-sun fa-fw" style="color: #868B94;"></i> <span class="ms-1">{uv_index}</span>
                    </div>
                  </div>
                  <div>
                    <img src="{icon}"
                      width="100px">
                  </div>
                </div>
              </div>
            </div>
              </div>
            </div>
          </div>
        </section>
    </body>
    """
    return HTMLResponse(content=html_content, status_code=200)