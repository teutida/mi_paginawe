import React from 'react';
//import Title from 'antd/lib/typography/Title';

import { List, Avatar, Space } from 'antd';
import { MessageOutlined, LikeOutlined, StarOutlined } from '@ant-design/icons';

const IconText = ({ icon, text }) => (
	<Space>
		{React.createElement(icon)}
		{text}
	</Space>
);

const Blog = (props) => {
	return (
		<List
			itemLayout="vertical"
			size="large"
			pagination={{
				onChange: (page) => {
					console.log(page);
				},
				pageSize: 5,
			}}
			dataSource={props.data}
			footer={
				<div>
					<b>Swedish House Mayan Corporation</b>
				</div>
			}
			renderItem={(item) => (
				<List.Item
					key={item.title}
					actions={[
						<IconText
							icon={StarOutlined}
							text="156"
							key="list-vertical-star-o"
						/>,
						<IconText
							icon={LikeOutlined}
							text="156"
							key="list-vertical-like-o"
						/>,
						<IconText
							icon={MessageOutlined}
							text="2"
							key="list-vertical-message"
						/>,
					]}
					extra={
						<img
							width={272}
							alt="logo"
							src="https://gw.alipayobjects.com/zos/rmsportal/mqaQswcyDLcXyDKnZfES.png"
						/>
					}
				>
					<List.Item.Meta
						avatar={<Avatar src={item.avatar} />}
						//todo las variables son de ley en ingles papitos.
						title={<a href={`/${item.slug}`}>{item.titulo}</a>}
						description={item.descripcion}
					/>
					{item.content}
				</List.Item>
			)}
		/>
	);
};

export default Blog;
