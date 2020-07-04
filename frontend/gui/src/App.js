import React from 'react';
//import './App.css';
import { Component } from 'react';
import 'antd/dist/antd.css';
//import ReacDOM from 'react-dom';

import CustomLayout from './contenedores/layaout';
import BaseRoute from './rounter';
import { BrowserRouter as Router } from 'react-router-dom';

/*function App() {
	return (
		<div className="App">
			<CustomLayout>
				<ListBlog />
			</CustomLayout>
		</div>
	);
}*/

class App extends Component {
	render() {
		return (
			<div className="App">
				<Router>
					<CustomLayout>
						<BaseRoute />
					</CustomLayout>
				</Router>
			</div>
		);
	}
}

export default App;
