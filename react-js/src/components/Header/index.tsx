import { Link } from 'react-router-dom';

export default function Header() {
    return (
        <header>
            <button>menu</button>
            <div>
                <img src="" alt=""/>
                <div>
                    <h1>name</h1>
                    <Link />
                </div>
            </div>
            <div>
                <Link />
                <Link />
                <LibraryRecomenda></LibraryRecomenda>
            </div>
        </header>
    );
}