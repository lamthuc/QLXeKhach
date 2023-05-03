import axios from "axios";

export const endpoints = {
    'chuyenxe': '/chuyenxe/',
    'tuyenxe': '/tuyenxe/'
}

export default axios.create({
    baseURL: "http://127.0.0.1:8000/" 
    
})