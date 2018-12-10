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
    for (let id in results) {
      if (results[id].hasOwnProperty('public_scores')) {
        let totalScore = 0;
        for (let no in results[id].public_scores) {
          totalScore += results[id].public_scores[no];
          if (results[id].hasOwnProperty('private_scores')) {
            totalScore += results[id].private_scores[no];
          }
        }
        totalScore += results[id].flake8
        totalScore +=20 // pr score baseline
        rows.push({
          'student_id': id,
          'flake8': results[id].flake8,
          'public_scores': results[id].public_scores,
          'private_scores': results[id].private_scores,
          'total_scores': totalScore,
          'pr_scores': 20 // pr score baseline
        });
      }
    }
    let customHeadStyle = {
      'padding': '0.5em',
      'textAlign': 'center'
    }

    rows = rows.map((row, idx) => {
      return (
        <TableRow key={idx}>
          <TableCell component='th' scope='row' style={customHeadStyle}>
            {row.student_id}
          </TableCell>
          <TableCell numeric style={customHeadStyle}>{row.flake8}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.public_scores['1']}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.public_scores['2']}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.public_scores['3']}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.public_scores['4']}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.public_scores['5']}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.public_scores['6']}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.public_scores['7']}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.public_scores['8']}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.private_scores ? row.private_scores['1'] : '?'}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.private_scores ? row.private_scores['2'] : '?'}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.private_scores ? row.private_scores['3'] : '?'}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.private_scores ? row.private_scores['4'] : '?'}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.private_scores ? row.private_scores['5'] : '?'}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.private_scores ? row.private_scores['6'] : '?'}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.private_scores ? row.private_scores['7'] : '?'}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.private_scores ? row.private_scores['8'] : '?'}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.coding_style ? row.coding_style : '?'}</TableCell>
          <TableCell numeric style={customHeadStyle}>{row.pr_scores}</TableCell>
          <TableCell numeric style={{...customHeadStyle, color: row.total_scores >= 60 ? 'green':'red'}}>{row.total_scores}</TableCell>
        </TableRow>
      )
    })
    return (
      <div>
        <Paper className={classes.root}>
          <Table className={classes.table} >
            <colgroup>
              <col style={{width:'10%', background:'#DCDCDC'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'4%'}}/>
              <col style={{width:'10%'}}/>
            </colgroup>
            <TableHead>
              <TableRow>
                <TableCell style={customHeadStyle}>ID</TableCell>
                <TableCell style={customHeadStyle}>Flake8</TableCell>
                <TableCell style={customHeadStyle}>Pub1</TableCell>
                <TableCell style={customHeadStyle}>Pub2</TableCell>
                <TableCell style={customHeadStyle}>Pub3</TableCell>
                <TableCell style={customHeadStyle}>Pub4</TableCell>
                <TableCell style={customHeadStyle}>Pub5</TableCell>
                <TableCell style={customHeadStyle}>Pub6</TableCell>
                <TableCell style={customHeadStyle}>Pub7</TableCell>
                <TableCell style={customHeadStyle}>Pub8</TableCell>
                <TableCell style={customHeadStyle}>Pri2</TableCell>
                <TableCell style={customHeadStyle}>Pri3</TableCell>
                <TableCell style={customHeadStyle}>Pri4</TableCell>
                <TableCell style={customHeadStyle}>Pri5</TableCell>
                <TableCell style={customHeadStyle}>Pri6</TableCell>
                <TableCell style={customHeadStyle}>Pri7</TableCell>
                <TableCell style={customHeadStyle}>Pri8</TableCell>
                <TableCell style={customHeadStyle}>Style</TableCell>
                <TableCell style={customHeadStyle}>PR</TableCell>
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
