"use client";
import {useRef} from 'react';

import io from 'socket.io-client';

const socket = io("http://localhost:3000/")

interface ChatProps {};

const Chat = ({}: ChatProps) => {
	const messageRef = useRef<HTMLInputElement | null>(null);

	const sendMessage = () => {
		if (messageRef.current != null) {
			console.log(messageRef.current?.value);
			socket.emit("message", messageRef.current?.value);
		}
	};
	return (
		<main className='flex ml-10 mt-10'>
			<input ref={messageRef} className='border-red-500' type='text' placeholder='Type something ...'></input>
			<button
				className='border-black'
				onClick={sendMessage}
			>
				Send!
			</button>
		</main>
	)
}

export default Chat;
