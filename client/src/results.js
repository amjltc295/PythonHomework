import React, { Component } from 'react';

import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';


const classes = theme => ({
    root: {
      width: '100%',
      marginTop: theme.spacing.unit * 3,
    },
    table: {
      width: '80%',
    },
});


let id = 0;
function createData(student_id, pr, t1, t2, t3, t4, t5, t6, t7, t8, flake8, codingStyle, total) {
  id += 1;
  return { id, student_id, pr, t1, t2, t3, t4, t5, t6, t7, t8, flake8, codingStyle, total};

}

const rows = [
  createData('test_id', 20, 1, 2, 3, 4, 5, 6, 7 ,8, 10, 10, 100),
];

class ResultTable extends Component {
  constructor(props) {
    super(props);

    this.state = {
      loading: true,
      results: {}
    };
  }
  componentDidMount() {
    this.fetchResults();
  }
  fetchResults() {
    let get_results_url = 'http://localhost:15000/get_results';
    fetch(get_results_url).then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Something went wrong');
      }
    })
    .then((responseJson) => {
      console.log(responseJson.results);
      let results = JSON.stringify(responseJson);
      this.setState(
        {
          loading: false,
          results: results
        }
      );
      console.log(responseJson);
      return responseJson;
    })
    .catch((error) => {
        console.log(error)

    });
  }
  render() {
    let {loading, results} = this.state;
    if (loading) {
      return null;
    }
    return (
      <div>
        <Paper className={classes.root}>
          <Table className>
            <TableHead>
              <TableRow>
                <TableCell>Student ID</TableCell>
                <TableCell numeric>PR</TableCell>
                <TableCell numeric>Task 1</TableCell>
                <TableCell numeric>Task 2</TableCell>
                <TableCell numeric>Task 3</TableCell>
                <TableCell numeric>Task 4</TableCell>
                <TableCell numeric>Task 5</TableCell>
                <TableCell numeric>Task 6</TableCell>
                <TableCell numeric>Task 7</TableCell>
                <TableCell numeric>Task 8</TableCell>
                <TableCell numeric>Flake8 Check</TableCell>
                <TableCell numeric>Coding Style</TableCell>
                <TableCell numeric>Total Score</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {rows.map(row => {
                return (
                  <TableRow key={row.id}>
                    <TableCell component="th" scope="row">
                      {row.student_id}
                    </TableCell>
                    <TableCell numeric>{row.pr}</TableCell>
                    <TableCell numeric>{row.t1}</TableCell>
                    <TableCell numeric>{row.t2}</TableCell>
                    <TableCell numeric>{row.t3}</TableCell>
                    <TableCell numeric>{row.t4}</TableCell>
                    <TableCell numeric>{row.t5}</TableCell>
                    <TableCell numeric>{row.t6}</TableCell>
                    <TableCell numeric>{row.t7}</TableCell>
                    <TableCell numeric>{row.t8}</TableCell>
                    <TableCell numeric>{row.flake8}</TableCell>
                    <TableCell numeric>{row.codingStyle}</TableCell>
                    <TableCell numeric>{row.total}</TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </Paper>

        <h5> Results: {results} </h5>
      </div>
    )
  }
}

export default ResultTable;
