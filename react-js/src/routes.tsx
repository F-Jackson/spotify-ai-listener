import App from "pages/App";
import Configs from "pages/Configs";
import Index from "pages/Index";
import LibraryList from "pages/LibrarysList";
import LibraryDetail from "pages/LibraryDetail";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { RecoilRoot } from "recoil";


export default function Router() {
    return (
        <BrowserRouter>
            <RecoilRoot>
                <Routes>
                    <Route path="/" element={<App />}>
                        <Route index element={<Index />} />
                        <Route path="configs" element={<Configs />} />
                        <Route path="librarys" element={<LibraryList />} />
                        <Route path="library/:id" element={<LibraryDetail />} />
                    </Route>
                </Routes>
            </RecoilRoot>
        </BrowserRouter>
    );
}