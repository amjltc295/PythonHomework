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
    let get_results_url = process.env.REACT_APP_ENDPOINT + '/get_results';
    fetch(get_results_url).then((response) => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('Something went wrong');
      }
    })
    .then((responseJson) => {
      console.log(responseJson.results);
      let results = responseJson;
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
    results = results.results;
    let rows = []
    for(let id in results){
        if (results[id].hasOwnProperty('public_scores')){
          let totalScore = 0;
          for(let no in results[id].public_scores){
            totalScore += results[id].public_scores[no];
            totalScore += results[id].private_scores[no];
          }
          totalScore += results[id].flake8
          rows.push({
            "student_id": id,
            "flake8": results[id].flake8,
            "public_scores": results[id].public_scores,
            "private_scores": results[id].private_scores,
            "total_scores": totalScore
          });
      }
    }

    
    rows = rows.map((row, idx) => {
      return (
        <TableRow key={idx}>
          <TableCell component="th" scope="row">
            {row.student_id}
          </TableCell>
          <TableCell numeric>{row.flake8}</TableCell>
          <TableCell numeric>{row.public_scores["1"]}</TableCell>
          <TableCell numeric>{row.public_scores["2"]}</TableCell>
          <TableCell numeric>{row.public_scores["3"]}</TableCell>
          <TableCell numeric>{row.public_scores["4"]}</TableCell>
          <TableCell numeric>{row.public_scores["5"]}</TableCell>
          <TableCell numeric>{row.public_scores["6"]}</TableCell>
          <TableCell numeric>{row.public_scores["7"]}</TableCell>
          <TableCell numeric>{row.public_scores["8"]}</TableCell>
          <TableCell numeric>{row.private_scores["1"]}</TableCell>
          <TableCell numeric>{row.private_scores["2"]}</TableCell>
          <TableCell numeric>{row.private_scores["3"]}</TableCell>
          <TableCell numeric>{row.private_scores["4"]}</TableCell>
          <TableCell numeric>{row.private_scores["5"]}</TableCell>
          <TableCell numeric>{row.private_scores["6"]}</TableCell>
          <TableCell numeric>{row.private_scores["7"]}</TableCell>
          <TableCell numeric>{row.private_scores["8"]}</TableCell>
          <TableCell numeric>{row.total_scores}</TableCell>
        </TableRow>
      )
    })
    let customHeadStyle = {
      "padding": "4px 22px 4px 11px"
    }
    return (
      <div>
        <Paper className={classes.root}>
          <Table className={classes.table} fixedHeader={false} style={{ width: "auto", tableLayout: "auto" }}>
            <TableHead>
              <TableRow>
                <TableCell style={customHeadStyle}>ID</TableCell>
                <TableCell style={customHeadStyle}>Flake8</TableCell>
                <TableCell style={customHeadStyle}>Public1</TableCell>
                <TableCell style={customHeadStyle}>Public2</TableCell>
                <TableCell style={customHeadStyle}>Public3</TableCell>
                <TableCell style={customHeadStyle}>Public4</TableCell>
                <TableCell style={customHeadStyle}>Public5</TableCell>
                <TableCell style={customHeadStyle}>Public6</TableCell>
                <TableCell style={customHeadStyle}>Public7</TableCell>
                <TableCell style={customHeadStyle}>Public8</TableCell>
                <TableCell style={customHeadStyle}>Private1</TableCell>
                <TableCell style={customHeadStyle}>Private2</TableCell>
                <TableCell style={customHeadStyle}>Private3</TableCell>
                <TableCell style={customHeadStyle}>Private4</TableCell>
                <TableCell style={customHeadStyle}>Private5</TableCell>
                <TableCell style={customHeadStyle}>Private6</TableCell>
                <TableCell style={customHeadStyle}>Private7</TableCell>
                <TableCell style={customHeadStyle}>Private8</TableCell>
                <TableCell style={customHeadStyle}>Score</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {rows}
            </TableBody>
          </Table>
        </Paper>
      </div>
    )
  }
}

export default ResultTable;
