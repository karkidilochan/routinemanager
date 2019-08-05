import React, { Component } from 'react';
import CustomersService from './DepartmentsService';

const departmentsService = new DepartmentsService();

class DepartmentCreateUpdate extends Component {
    constructor(props) {
        super(props);

        this.handleSubmit = this.handleSubmit.bind(this);
      }

      componentDidMount(){
        const { match: { params } } = this.props;
        if(params && params.pk)
        {
          departmentsService.getDepartment(params.pk).then((c)=>{
            this.refs.departmentid.value = c.departmentid;
            this.refs.departmentname.value = c.departmentname;
          })
        }
      }

      handleCreate(){
        departmentsService.createDepartment(
          {
            "Department": this.refs.departmentid.value,
            "Name": this.refs.departmentname.value,
        }          
        ).then((result)=>{
          alert("Department created!");
        }).catch(()=>{
          alert('There was an error! Please re-check your form.');
        });
      }
      handleUpdate(pk){
        departmentsService.updateDepartment(
          {
            "pk": pk,
            "first_name": this.refs.departmentid.value,
            "last_name": this.refs.departmentname.value,
        }          
        ).then((result)=>{
          console.log(result);
          alert("Department updated!");
        }).catch(()=>{
          alert('There was an error! Please re-check your form.');
        });
      }
      handleSubmit(event) {
        const { match: { params } } = this.props;

        if(params && params.pk){
          this.handleUpdate(params.pk);
        }
        else
        {
          this.handleCreate();
        }

        event.preventDefault();
      }

      render() {
        return (
          <form onSubmit={this.handleSubmit}>
          <div className="form-group">
            <label>
              Department:</label>
              <input className="form-control" type="text" ref='departmentid />

            <label>
              Name:</label>
              <input className="form-control" type="text" ref='departmentname'/>



            <input className="btn btn-primary" type="submit" value="Submit" />
            </div>
          </form>
        );
      }  
}

export default DepartmentCreateUpdate;