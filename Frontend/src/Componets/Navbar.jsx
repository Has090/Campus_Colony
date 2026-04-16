
export function Navbar(){
  const array=[{
    name:"Home",
    path:"/",
  },
  {
    name:"Area insight",
    path:"/Area"
  },
  {
    name:"AI Assistant",
    path:"/AI"
  },
  {
    name:"Contact us",
    path:"/contact-us"
  },
  {
    name:"About us",
    path:"/About-us" 
  }]
  return (
    <nav className="flex flex-row justify-around mt-3 border-amber-900 border-2 rounded-lg p-2">
       <img src="/logo.png"  alt="Map" className="w-[45px] grayscale hover:grayscale-0 transition-all duration-500" />
       <ul
       className="flex flex-row justify-between w-[40%]">
        {
          array.map((item)=>(
            <li key={item.name}>
            <a href={item.path}>
              {item.name}
            </a>
            </li>
          ))
        }
       </ul>
     </nav>
   )
} 