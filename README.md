<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Axel3246/Smart-TrafficAgent-TEC">
    <img src="./Images/TLogo.jpeg" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Smart Traffic Agent for ITESM's Roundabout</h3>

  <p align="center">
    This project uses agent.py and Unity to model and simulate <br/>
    an agent capable of resolving ITESM's roundabout traffic problem.
    <br /><br />
    <a href="https://drive.google.com/drive/folders/14CkqHgOAIuTdzL1cLgOgP30bt8ABbcis?usp=sharing"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://drive.google.com/file/d/1x1VTxBMP88dZhI_Mhj-ZAJsGYBUmotuv/view?usp=share_link">View Live Demo</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributors</a></li>
    <li><a href="#license">License</a></li>

  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

<div align="center">
  <img src="./Images/rgs.jpeg" width="60%" height="60%">
</div>
<br>

Currently, one of the main problems in any city and metropolis is traffic. The exponential increase of habitants has allowed this to become more frequent and increasingly common on the streets, avenues, intersections, and crossroads of cities. Various infrastructure, such as bridges or roundabouts, has been installed with the aim of avoiding this, but they do not always have the necessary efficiency to solve the problem.

The roundabout located at Garza Sada and Av. del Estado is one of the busiest in Distrito Tec. It was remodeled back in 2017 due to the high incidence of car accidents recorded in 2015 (86). This allowed pedestrians and drivers to enjoy various improvements, such as the expansion of roadways and sidewalks, increased lighting, the leveling of sidewalks and pavement, etc. There was synchronization between traffic lights, which theoretically would allow for better vehicle and pedestrian flow. However this feature cannot be seen during the busiest hours of the roundabout and its avenues allowing traffic accumulation, thus slowing the flow.

That leads us to the purpose of this project, which is to carry out a simulation with agent and computational graphics that allows to improve the vehicle flow in the Garza Sada and Av. del Estado roundabout. The simulation consists of two solutions described below:
<br></br>

* <strong>Roundabout Remodeling</strong>: It is expected that by removing or disabling some elements that make up the roundabout, such as, for example, a pair of traffic lights, the flow of traffic can greatly improve during highly traveled hours.

* <strong>Use of Smart Traffic Lights</strong>: Due to the new restructuring of the roundabout, it is expected that by introducing a new artificial intelligence system of smart traffic lights, it will be possible to maintain the privileges and benefits of pedestrians and drivers, as well as better traffic flow due to fast decision making depending on the amount of vehicles coming from Av. Garza Sada and Av. del Estado.

<p align="right">(<a href="#readme-top">Take me up!</a>)</p>

### Built With
The technologies that made possible this project are shown below.

* ![C#](https://img.shields.io/badge/c%23-%23239120.svg?style=for-the-badge&logo=c-sharp&logoColor=white)
* ![Unity](https://img.shields.io/badge/unity-%23000000.svg?style=for-the-badge&logo=unity&logoColor=white)
* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

<p align="right">(<a href="#readme-top">Take me up!</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

1. Be sure to have the lastest version of Python available in your computer. <a href="https://www.python.org/downloads/">Download Python </a> from the official website if you do not currently possess the lastest version.

2. Verify you have pip installed in your computer. You can check by running the following command in your terminal.

* Check pip version
  ```sh
  pip3 --version.
  ```
### Installation

1. Install Unity Hub and be sure to set it's version to <a href="https://unity.com/releases/editor/whats-new/2021.3.8">2021.3.8</a>.

2. Install any IDE of your choice. For this project we recommend <a href="https://code.visualstudio.com/"> Visual Studio Code</a>.

3. Clone the repo
   ```sh
   git clone https://github.com/Axel3246/Smart-TrafficAgent-TEC
   ```

4. Once you clone the repo, open the `Simulation-DataServer` folder and go to `tc2008B_server.py` file. Change the port in the following line to any unused localhost port in your computer.
   ```py
   def run(server_class=HTTPServer, handler_class=Server, port=YOURPORT):
   ```

5. Unzip `Unity-TSTEC.zip` and move the folder to Unity Hub. Open it and go to <strong>Scripts > v3.1.2022 > </strong> `clon.cs`. Change the port in the following line to any unused port in your computer. <strong> This needs to match </strong> `tc2008B_server.py`<strong> port</strong>.
   ```cs
   string url = "http://localhost:YOURPORT";
   ```

<p align="right">(<a href="#readme-top">Take me up!</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

<div align="center">
  <img src="https://github.com/Axel3246/MisCompas-WebApp/blob/main/Images/Rating.png?raw=true" width="45%" height="45%">
  <p align="center">
    Rating Screen
    <br/>
  </p>
</div>

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">Take me up!</a>)</p>

<!-- CONTRIBUTING -->
## Contributors

Here you'll find the team that made possible this project. Feel free to check out their GitHub profiles too!

<a href="https://github.com/axel3246/Smart-TrafficAgent-TEC/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=axel3246/Smart-TrafficAgent-TEC" />
</a>

<p align="right">(<a href="#readme-top">Take me up!</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">Take me up!</a>)</p>
