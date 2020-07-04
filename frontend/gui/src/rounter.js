import React from 'react';
import { Route } from 'react-router-dom';
import ListBlog from './contenedores/listview';

import DetailBlog from './contenedores/detailview';

const BaseRoute = () => (
	<div>
		<Route exact path="/" component={ListBlog} />
		<Route exact path="/:slugID" component={DetailBlog} />
	</div>
);

export default BaseRoute;
