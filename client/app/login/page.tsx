const Login = () => {
	return (
		<main className='w- h-full text-center m-auto-auto'>
			<section className='container bg-blue-200 border-black-300 rounded-lg w-4/12 h-6/12'>
				<input type='text' placeholder='username'></input>
				<br/>
				<input type='password' placeholder='password'></input>
				<br/>
				<div className='font-semibold'>Forgot Password</div>
				<div className='font-semibold hover:underline'>Already have an account? Sign in.</div>
			</section>
		</main>
	)
}

export default Login;
