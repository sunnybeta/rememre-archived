import Image from "next/image";
import Link from "next/link";

export default function Home() {
	return (
		<main className='h-screen box'>
			<section className='absolute h-screen -z-10 inset-0'>
				<Image
					alt='rememre-background'
					src="/bg.jpg"
					layout="fill"
					objectFit="cover"
					quality={100}
				/>
			</section>
			<header className="h-24 w-full flex justify-between items-center bg-transparent">
				<section className="flex items-center px-8">
					<Image src="/logo.png" alt="Logo" width={50} height={30} />
					<div className="text-4xl px-4">rememre</div>
				</section>
				<nav>
					<ul className="mx-3">
						<Link className="px-3 hover:underline" href="/about">ABOUT</Link>
						<Link className="px-3 hover:underline" href="/contact">CONTACT</Link>
						<Link className="px-3 hover:underline" href="/login">LOGIN</Link>
					</ul>
				</nav>
			</header>
			<div className='text-7xl w-full text-center mt-64'>
				Learn Smarter, Not Harder
			</div>
		</main>
	)
}
