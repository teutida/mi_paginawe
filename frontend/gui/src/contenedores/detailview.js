import React from 'react';
import axios from 'axios';

import { Card } from 'antd';

class DetailBlog extends React.Component {
	state = {
		blog: {},
	};

	componentDidMount() {
		const slugID = this.props.match.params.slugID;
		axios.get(`http://localhost:8000/api/${slugID}`).then((res) => {
			this.setState({
				blog: res.data,
			});
		});
	}
	render() {
		return (
			<Card title={this.state.blog.titulo}>
				<p>{this.state.blog.fecha_publicacion}</p>
				<p>{this.state.blog.descripcion}</p>
				<p>{this.state.blog.cuerpo}</p>
			</Card>
		);
	}
}

export default DetailBlog;
