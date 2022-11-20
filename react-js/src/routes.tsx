import App from "pages/App";
import Configs from "pages/Configs";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { RecoilRoot } from "recoil";

export default function Router() {
    return (
        <BrowserRouter>
            <RecoilRoot>
                <Routes>
                    <Route path="/" element={<App />}>
                        <Route path="configs" element={<Configs />} />
                    </Route>
                </Routes>
            </RecoilRoot>
        </BrowserRouter>
    );
}