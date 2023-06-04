import ClassChooser from "../components/ClassChooser";
import Equipment from "../components/Equipment";

const Templater = () => {
  return (
    <>
        <div className="mt-3 mb-3 py-0.5 px-4 text-2xl text-center bg-custom-gray text-custom-white rounded-md">
          Template Builder
        </div>
        <ClassChooser />

        <div className="mt-5 grid grid-cols-5 gap-5">
            <Equipment />
            <Equipment />
            <Equipment />
            <Equipment />
            <Equipment />
            <Equipment />
            <div className="col-span-3" />
            <Equipment />
            <Equipment />
            <div className="col-span-3" />
            <Equipment />
            <Equipment />
            <div className="col-span-3" />
            <Equipment />
            <Equipment />
            <div className="col-span-3" />
            <Equipment />
            <Equipment />
            <div className="col-span-3" />
            <Equipment />
        </div>
        <div className="mt-5 flex flex-center gap-11">            
            <Equipment />
            <Equipment />
            <Equipment />
            <Equipment />
        </div>

        <section className="mt-5 flex flex-col flex-center w-full bg-custom-blue rounded-md">
            <div className="mt-5 mb-3 py-0.5 px-4 text-2xl w-44 text-center bg-custom-gray text-custom-white rounded-md">
                Report
            </div>
            <div>
                <span className="flex flex-wrap gap-4">
                <div className="mb-5 px-1 bg-custom-white rounded-md">
                        <div className="basis-full font-semibold">
                            Stats
                        </div>
                        <div className="h-1 bg-custom-gray" />
                        <ol class="list-none">
                            <li>Strength:</li>
                            <li>Dexterity:</li>
                            <li>Constitution:</li>
                            <li>Piety:</li>
                            <li>Intelligence:</li>
                            <li>Charisma:</li>
                            <li>Armor Factor:</li>
                        </ol>
                    </div>
                    <div className="mb-5 px-1 bg-custom-white rounded-md">
                        <div className="basis-full font-semibold">
                            Resists    
                        </div>
                        <div className="h-1 bg-custom-gray" />
                        <ol>
                            <li>Slash:</li>
                            <li>Thrust:</li>
                            <li>Crush:</li>
                            <li>Body:</li>
                            <li>Spirit:</li>
                            <li>Energy:</li>
                            <li>Heat:</li>
                            <li>Matter:</li>
                            <li>Cold:</li>
                        </ol>
                    </div>
                    <div className="mb-5 px-1 bg-custom-white rounded-md">
                        <div className="basis-full font-semibold">
                            Skills
                        </div>
                        <div className="h-1 bg-custom-gray" />
                        <ol>
                            <li>Pacification:</li>
                            <li>Augmentation:</li>
                            <li>Mending:</li>
                        </ol>
                    </div>
                    <div className="mb-5 px-1 bg-custom-white rounded-md">
                        <div className="basis-full font-semibold">
                            ToA Bonuses
                        </div>
                        <div className="h-1 bg-custom-gray" />
                        <ol>
                        <li>Melee Speed:</li>
                        <li>Melee Damage:</li>
                        <li>Casting Speed:</li>
                        <li>Spell Damage:</li>
                        <li>Spell Range:</li>
                        <li>Resistance Pierce:</li>
                        <li>Buff Bonus:</li>
                        <li>Heal Bonus:</li>
                        <li>Spell Duration:</li>
                        </ol>
                    </div>
                    <div className="mb-5 px-1 bg-custom-white rounded-md">
                        <div className="basis-full font-semibold">
                            Other Bonuses
                        </div>
                        <div className="h-1 bg-custom-gray" />
                        <ol>
                            <li>Arcane Siphon:</li>
                            <li>Myth Power Regen:</li>
                            <li>Myth Health Regen:</li>
                            <li>CC Reduction:</li>
                            <li>Conversion:</li>
                        </ol>
                    </div>
                </span>
            </div>
        </section>
    </>
    )
}

export default Templater