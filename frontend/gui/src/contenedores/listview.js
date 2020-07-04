import React from 'react';
import axios from 'axios';

import Blog from '../componentes/Blog';

class ListBlog extends React.Component {
	state = {
		blog: [],
	};

	componentDidMount() {
		axios.get('http://localhost:8000/api/').then((res) => {
			this.setState({
				blog: res.data,
			});
		});
	}
	render() {
		return <Blog data={this.state.blog} />;
	}
}

export default ListBlog;
