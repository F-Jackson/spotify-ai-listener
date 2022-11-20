import Input from "./components/Inputs";

export default function Configs() {
    return (
        <section>
            <form action="">
                <button type="submit">Save</button>
                <div>
                    <img src="" alt="" />
                </div>
                <div>
                    <Input 
                        type="text"
                        name='username'
                        placeholder="Username"
                    />
                    <Input 
                        type="text"
                        name='email'
                        placeholder="Email"
                    />
                    <div>
                        <Input />
                        <Input />
                    </div>
                    <Input />
                    <div>
                        <Input />
                        <Input />
                    </div>
                </div>
                <div>
                    <Input />
                    <Input />
                    <Input />
                    <Input />
                    <Input />
                </div>
            </form>
        </section>
    );
}