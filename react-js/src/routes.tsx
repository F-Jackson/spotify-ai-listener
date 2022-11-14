import Footer from "components/Footer";
import Header from "components/Header";
import Template from "components/Template";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { RecoilRoot } from "recoil";

export default function Router() {
    return (
        <BrowserRouter>
            <RecoilRoot>
                <Header />
                <Routes>
                    <Route path="" element={<Template></Template>}>
                        
                    </Route>
                </Routes>
                <Footer />
            </RecoilRoot>
        </BrowserRouter>
    );
}