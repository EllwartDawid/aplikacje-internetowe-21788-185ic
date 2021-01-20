
# Lab10 Django + React (aplikacja TODO)


# Wygląd strony backend

![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium10/ss/przyklad2.PNG)

# Wygląd strony dodwania


![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium10/ss/dodawanietodo.PNG)

# Widok dodanego elementu


![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium10/ss/dodanetodo.PNG)

# Wygląd końcowy strony z frontendem

# Wygląd strony dodwania

![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium10/ss/dodawaniefront.PNG)

# Widok dodanego elementu


![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium10/ss/dodanyfront.PNG)

# complete


![App](https://github.com/EllwartDawid/aplikacje-internetowe-21788-185ic/blob/master/Laboratorium10/ss/complete.PNG)

Do pliku `setting.py` dodajemy nastepujący kod:

```javascript
INSTALLED_APPS = [
    'rest_framework',
    'todo',
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]
```

W tutorialu jest pokazane, że także trzeba dodać do pliku `setting.py`:

```javascript
CORS_ORIGIN_WHITELIST = (
     'localhost:3000/'
 )
```

Natomiast ja zmodyfikowałem powyższy kod ponieważ bez modyfikacji pojawiał sie błąd. Kod powinien wyglądać następująco:

```javascript
CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://localhost:8000',
    'http://localhost:8080',
)
```

Tworzymy plik `models.py`:

```javascript
from django.db import models

# Create your models here.
class Todo(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  completed = models.BooleanField(default=False)

  def _str_(self):
    return self.title
```

Tworzę `TodoSerializer`, klasę która będzie zarządzać serializacją i deserializacją

```javascript
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Todo
    fields = ('id', 'title', 'description', 'completed')
```

Tworzę urls.py, które określa ścieżkę adresu URL dla interfejsu API:

```javascript
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views

router = routers.DefaultRouter()
router.register(r'todos', views.TodoView, 'todo')

urlpatterns = [
    path('admin/', admin.site.urls),         path('api/', include(router.urls))
]
```

Tworze widoki:

```javascript
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo

class TodoView(viewsets.ModelViewSet):
  serializer_class = TodoSerializer
  queryset = Todo.objects.all()
```

## FRONTED React-TODO

Żeby zacząć pracę należy stworzyc aplikację:

Instalujemy urządzenie:

`npm install -g create-react-app`

Tworzymy aplikację:

`create-react-app frontend` 

Zaimportujemy arkusz stylów Bootstrap w `src/index.js`, abyśmy mogli używać klas Bootstrap:
```javascript
import 'bootstrap/dist/css/bootstrap.min.css';
```

Edytujemy index.css:

```javascript
body {
    margin: 0;
    padding: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen",
      "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue",
      sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    background-color: #282c34;
  }
  .todo-title {
    cursor: pointer;
  }
  .completed-todo {
    text-decoration: line-through;
  }
  .tab-list > span {
    padding: 5px 8px;
    border: 1px solid #282c34;
    border-radius: 10px;
    margin-right: 5px;
    cursor: pointer;
  }
  .tab-list > span.active {
    background-color: #282c34;
    color: #ffffff;
  }
```

Należy dołączyć plik `Modal.js`:

```javascript
import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem
    };
  }
  handleChange = e => {
    let { name, value } = e.target;
    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }
    const activeItem = { ...this.state.activeItem, [name]: value };
    this.setState({ activeItem });
  };
  render() {
    const { toggle, onSave } = this.props;
    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}> Todo Item </ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="title">Title</Label>
              <Input
                type="text"
                name="title"
                value={this.state.activeItem.title}
                onChange={this.handleChange}
                placeholder="Enter Todo Title"
              />
            </FormGroup>
            <FormGroup>
              <Label for="description">Description</Label>
              <Input
                type="text"
                name="description"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter Todo description"
              />
            </FormGroup>
            <FormGroup check>
              <Label for="completed">
                <Input
                  type="checkbox"
                  name="completed"
                  checked={this.state.activeItem.completed}
                  onChange={this.handleChange}
                />
                Completed
              </Label>
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button color="success" onClick={() => onSave(this.state.activeItem)}>
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}
```
Edytujemy `App.js`:

```javascript
import React, { Component } from "react";
import Modal from "./components/Modal";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      viewCompleted: false,
      activeItem: {
        title: "",
        description: "",
        completed: false
      },
      todoList: []
    };
  }
  componentDidMount() {
    this.refreshList();
  }
  refreshList = () => {
    axios
      .get("http://localhost:8000/api/todos/")
      .then(res => this.setState({ todoList: res.data }))
      .catch(err => console.log(err));
  };
  displayCompleted = status => {
    if (status) {
      return this.setState({ viewCompleted: true });
    }
    return this.setState({ viewCompleted: false });
  };
  renderTabList = () => {
    return (
      <div className="my-5 tab-list">
        <span
          onClick={() => this.displayCompleted(true)}
          className={this.state.viewCompleted ? "active" : ""}
        >
          complete
        </span>
        <span
          onClick={() => this.displayCompleted(false)}
          className={this.state.viewCompleted ? "" : "active"}
        >
          Incomplete
        </span>
      </div>
    );
  };
  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.todoList.filter(
      item => item.completed === viewCompleted
    );
    return newItems.map(item => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2 ${
            this.state.viewCompleted ? "completed-todo" : ""
          }`}
          title={item.description}
        >
          {item.title}
        </span>
        <span>
          <button
            onClick={() => this.editItem(item)}
            className="btn btn-secondary mr-2"
          >
            {" "}
            Edit{" "}
          </button>
          <button
            onClick={() => this.handleDelete(item)}
            className="btn btn-danger"
          >
            Delete{" "}
          </button>
        </span>
      </li>
    ));
  };
  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };
  handleSubmit = item => {
    this.toggle();
    if (item.id) {
      axios
        .put(`http://localhost:8000/api/todos/${item.id}/`, item)
        .then(res => this.refreshList());
      return;
    }
    axios
      .post("http://localhost:8000/api/todos/", item)
      .then(res => this.refreshList());
  };
  handleDelete = item => {
    axios
      .delete(`http://localhost:8000/api/todos/${item.id}`)
      .then(res => this.refreshList());
  };
  createItem = () => {
    const item = { title: "", description: "", completed: false };
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  editItem = item => {
    this.setState({ activeItem: item, modal: !this.state.modal });
  };
  render() {
    return (
      <main className="content">
        <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
        <div className="row ">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="">
                <button onClick={this.createItem} className="btn btn-primary">
                  Add task
                </button>
              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}
export default App;
```
W pliku `package.json` należy dodać:

```javascript
"proxy": "http://localhost:8000",
```
