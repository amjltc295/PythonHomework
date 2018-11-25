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
            overflowX: 'auto',

    },
    table: {
            minWidth: 700,

    },

});


let id = 0;
function createData(name, calories, fat, carbs, protein) {
  id += 1;
  return { id, name, calories, fat, carbs, protein  };

}

const rows = [
  createData('Frozen yoghurt', 159, 6.0, 24, 4.0),
  createData('Ice cream sandwich', 237, 9.0, 37, 4.3),
  createData('Eclair', 262, 16.0, 24, 6.0),
  createData('Cupcake', 305, 3.7, 67, 4.3),
  createData('Gingerbread', 356, 16.0, 49, 3.9),

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
          <Table className={classes.table}>
            <TableHead>
              <TableRow>
                <TableCell>Dessert (100g serving)</TableCell>
                <TableCell numeric>Calories</TableCell>
                <TableCell numeric>Fat (g)</TableCell>
                <TableCell numeric>Carbs (g)</TableCell>
                <TableCell numeric>Protein (g)</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {rows.map(row => {
                return (
                  <TableRow key={row.id}>
                    <TableCell component="th" scope="row">
                      {row.name}
                    </TableCell>
                    <TableCell numeric>{row.calories}</TableCell>
                    <TableCell numeric>{row.fat}</TableCell>
                    <TableCell numeric>{row.carbs}</TableCell>
                    <TableCell numeric>{row.protein}</TableCell>
                  </TableRow>
                );
              })}
            </TableBody>
          </Table>
        </Paper>
        <p> Results: {results} </p>
      </div>
    )
  }
}

export default ResultTable;
