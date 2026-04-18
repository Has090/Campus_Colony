export function HomeIntroduction() {
  return (
    <div className="bg-[#1e272e] text-white p-12 flex flex-col md:flex-row items-center justify-between rounded-3xl border-b-8 border-[#ff5e57] shadow-2xl">
      
      <div className="max-w-xl">
        <p className="text-[#ff5e57] font-black mb-4 text-xs tracking-[0.3em] uppercase">
          #1 Student Rental Platform in Lahore
        </p>
        
        <h1 className="text-7xl font-black leading-[0.9] mb-6 uppercase tracking-tighter">
          Smart Rentals <br /> 
          <span className="text-gray-500">Near Your</span> <br /> 
          Campus
        </h1>
        
        <p className="text-gray-400 mb-8 text-lg font-medium border-l-4 border-[#ff5e57] pl-4">
          Find hostels, flats & homes within 5 km of your college in Lahore.<br />
          Get real area intelligence before you decide.
        </p>
        
        <div className="flex gap-4 mb-10">
          <a href="#" className="bg-[#ff5e57] hover:bg-[#ff3f34] text-white px-10 py-4 font-bold uppercase transition-all shadow-lg text-center">
            Explore Rentals
          </a>
          <a href="#" className="border-2 border-[#ff5e57] hover:bg-[#ff5e57] text-white px-10 py-4 font-bold uppercase transition-all hover:text-black text-center">
            Area Insights
          </a>
        </div>

        {/* Stats */}
        <div className="flex gap-12 pt-8 border-t border-[#ff5e57]">
          <div>
            <div className="text-3xl font-black text-[#ff5e57]">1200+</div>
            <div className="text-gray-500 text-[10px] font-bold uppercase tracking-widest">Listings</div>
          </div>
          <div>
            <div className="text-3xl font-black text-[#ff5e57]">15+</div>
            <div className="text-gray-500 text-[10px] font-bold uppercase tracking-widest">Campuses</div>
          </div>
          <div>
            <div className="text-3xl font-black text-[#ff5e57]">AI</div>
            <div className="text-gray-500 text-[10px] font-bold uppercase tracking-widest">Power</div>
          </div>
        </div>
      </div>

      {/* Right Content */}
      <div className="relative mt-12 md:mt-0">
        <div className="bg-[#1e272e] p-2 shadow-2xl rotate-2 border-2 border-[#ff5e57]">
           <img src="/intro.png" alt="Map" className="w-[450px] brightness-125 hover:brightness-150 transition-all duration-500" />
        </div>
        
        <div className="absolute -bottom-6 -left-10 bg-[#ff5e57] p-6 text-white border-4 border-[#ff5e57] -rotate-2 shadow-lg">
          <p className="font-black text-2xl uppercase italic leading-none">Faisal Town</p>
          <p className="text-xs font-bold mt-1 text-white tracking-tighter uppercase">Area Score: 86/100</p>
        </div>
      </div>

    </div>
  );
}