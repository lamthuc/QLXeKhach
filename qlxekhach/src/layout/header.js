import { useEffect } from "react"
import { useState } from "react"
import api, { endpoints } from "../configs/api"
import { Container, Nav, Navbar } from "react-bootstrap"
const Header = () => {
    const [chuyenxe, setChuyenXe] = useState([]) 
    useEffect(() => {
        const loadChuyenXe = async () => {
            let res = await api.get(endpoints['chuyenxe'])
            setChuyenXe(res.data)
        }
        loadChuyenXe()
    }, [])

    return (   
        <Navbar bg="light" expand="lg">
        <Container>
          <Navbar.Brand href="#home">WEBSITE QUẢN LÝ XE KHÁCH</Navbar.Brand>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="#home">Trang chủ</Nav.Link>
              <Nav.Link href="#link">Tuyến xe</Nav.Link>              
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>     
    )
}
export default Header