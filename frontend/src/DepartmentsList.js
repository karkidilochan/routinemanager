import  React, { Component } from  'react';
import  DepartmentsService  from './DepartmentsService';

const  departmentsService  =  new  DepartmentsService();

class  DepartmentsList  extends  Component {

constructor(props) {
    super(props);
    this.state  = {
        departments: [],
        nextPageURL:  ''
    };
    this.nextPage  =  this.nextPage.bind(this);
    this.handleDelete  =  this.handleDelete.bind(this);
}

componentDidMount() {
    var  self  =  this;
    departmentsService.getDepartment().then(function (result) {
        console.log(result);
        self.setState({ departments:  result.data, nextPageURL:  result.nextlink})
    });
}
handleDelete(e,pk){
    var  self  =  this;
    departmentsService.deleteDepartment({pk :  pk}).then(()=>{
        var  newArr  =  self.state.departments.filter(function(obj) {
            return  obj.pk  !==  pk;
        });

        self.setState({departments:  newArr})
    });
}

nextPage(){
    var  self  =  this;
    console.log(this.state.nextPageURL);        
    departmentsService.getDepartmentByURL(this.state.nextPageURL).then((result) => {
        self.setState({ departments:  result.data, nextPageURL:  result.nextlink})
    });
}
render() {

    return (
        <div  className="departments--list">
            <table  className="table">
            <thead  key="thead">
            <tr>
                <th>#</th>
                <th>Department id</th>
                <th>Department name</th>
            </tr>
            </thead>
            <tbody>
            {this.state.departments.map( c  =>
                <tr  key={c.pk}>
                <td>{c.pk}  </td>
                <td>{c.departmentid}</td>
                <td>{c.departmentname}</td>
                <td>
                <button  onClick={(e)=>  this.handleDelete(e,c.pk) }> Delete</button>
                <a  href={"/deparments/" + c.pk}> Update</a>
                </td>
            </tr>)}
            </tbody>
            </table>
            <button  className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button>
        </div>
        );
  }
}
export  default  DepartmentsList;