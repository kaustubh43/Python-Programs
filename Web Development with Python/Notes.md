# Web Development with python

Webserver
>A web server is software and hardware that uses HTTP (Hypertext Transfer Protocol)
> and other protocols to respond to client requests made over the World Wide Web.
> The main job of a web server is to display website content through storing, 
> processing and delivering webpages to users.
> 

### Running a webserver
1. cd to webserver folder
2. Create a virtual environment```python -m venv venv```
3. Activate the virtual environments ```.\venv\Scripts\activate```
4. Install requirements ```pip install -r requirements.txt ```
5. ```$env:FLASK_APP = "server.py"```
6. Run the server ```python -m flask run```
 
Voila! Your server is up and running. Copy the URL displayed in the terminal and paste it in your browser

> To run the server in debug mode
>
> Exit the server by doing a keyboard interrupt
> 
> 1. Run ```$env:FLASK_DEBUG=1```
> 2. Run the server again using ```python -m flask run```