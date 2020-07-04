import React from 'react';

import { Layout, Menu, Breadcrumb } from 'antd';

import { Link } from 'react-router-dom';

const { Header, Content, Footer } = Layout;

const CustomLayout = (props) => {
	return (
		<Layout className="layout">
			<Header>
				<div className="logo" />
				<Menu theme="dark" mode="horizontal" defaultSelectedKeys={['0']}>
					<Menu.Item key="1">Home</Menu.Item>
					<Menu.Item key="2">Categorias</Menu.Item>
					<Menu.Item key="3">Acerca de SHM</Menu.Item>
					<Menu.Item key="4">Programacion</Menu.Item>
					<Menu.Item key="6">Impresion 3D</Menu.Item>
				</Menu>
			</Header>
			<Content style={{ padding: '0 50px' }}>
				<Breadcrumb style={{ margin: '16px 0' }}>
					<Breadcrumb.Item>
						<Link to="/">Home</Link>
					</Breadcrumb.Item>
					<Breadcrumb.Item>
						<Link to="/">List</Link>
					</Breadcrumb.Item>
				</Breadcrumb>
				<div className="site-layout-content">{props.children}</div>
			</Content>
			<Footer style={{ textAlign: 'center' }}>
				Swedish House Mayan 2020 SWH
			</Footer>
		</Layout>
	);
};

export default CustomLayout;
