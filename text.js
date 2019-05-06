import React from 'react';
import axios from 'axios';
import { Button, Input} from 'reactstrap';
import { Col, Form, FormGroup, Label, Input, Button } from 'reactstrap';




class Profile extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            email: '',
            text: '',
        }
    }

    componentDidMount() {
        const token = localStorage.getItem('token');
        axios({
            method: 'GET',
            url: 'http://localhost:5000/api/v1/users/me/',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        }).then(response => {
            this.setState({
                user: response.data,
                email: this.state.email,
                text: this.state.text,
            })
        })
    }
    handleInput = (event) => {
        this.setState({
            [event.target.id]: event.target.value
        })
    }
    
    handleSave = (event) => {
        const token = localStorage.getItem('token');
        event.preventDefault();
        axios({
            method: 'POST',
            url: 'http://localhost:5000/api/v1/contact/',
            headers: {
                'Authorization': `Bearer ${token}`
            },
            data: {
                firstName: this.state.first_name,
                lastName: this.state.last_name,
            }
        }).then(response => {
            if (response.data.status === "success") {
            }
        })
            .catch(error => {
                console.log(error);
            })
    }

    render() {
        return (
            <div className="border m-5 p-5">
            <h1>Inquiry Form</h1>

            <Form onSubmit={this.handleSubmit}>
            <FormGroup row>
            <Label for="exampleEmail" sm={2}>Email</Label>
            <Col sm={10}>
            <Input type="email" name="email" id="email" value={this.state.email} onChange={this.handleInput} placeholder="" required/>
            </Col>
            </FormGroup>
            <FormGroup row>
            <Label for="exampleText" sm={2}>Text Area</Label>
            <Col sm={10}>
            <Input type="textarea" name="text" id="text" value={this.state.text} onChange={this.handleInput} placeholder="" required />
            </Col>
            </FormGroup>
        
            <FormGroup check row>
            <Col >
            <Button color="secondary" onClick={this.handleSave} >Submit</Button>
            </Col>
            </FormGroup>
            </Form>
            </div>
        )
    }



}

export default Profile;
