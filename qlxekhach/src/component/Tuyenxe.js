import { useEffect, useState } from "react"
import api, { endpoints } from "../configs/api"

const Tuyenxe = () => {
    const [tuyenxe, setTuyenxe] = useState([])
    useEffect(() => {
         const loadTuyenxe = async () => {
            let res = api.get(endpoints['tuyenxe'])
         }
    })
    return (
        <ul>
            
        </ul>
    )
}
export default Tuyenxe