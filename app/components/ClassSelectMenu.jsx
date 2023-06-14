import React from "react";
import { Dropdown as ClassSelect } from "@nextui-org/react";

export default function App() {
  const [realm, setRealm] = React.useState(new Set(["Choose your Class"]));

  const realmValue = React.useMemo(
    () => Array.from(realm).join(", ").replaceAll("_", " "),
    [realm]
  );

  return (
    <ClassSelect>
      <ClassSelect.Button css={{
        tt: "capitalize", 
        color: "secondary",
        borderRadius: 6,
        }}>
        {realmValue}
      </ClassSelect.Button>
      <ClassSelect.Menu
        aria-label="Single selection actions"
        color="secondary"
        disallowEmptySelection
        selectionMode="single"
        selectedKeys={realm}
        onSelectionChange={setRealm}
      >
        {/* TODO: Add images and colors to the dropdown items */}
        <ClassSelect.Item key="albion">Add</ClassSelect.Item>
        <ClassSelect.Item key="hibernia">Dynamic</ClassSelect.Item>
        <ClassSelect.Item key="midgard">Classes</ClassSelect.Item>
        <ClassSelect.Item key="midgard">Here</ClassSelect.Item>
      </ClassSelect.Menu>
    </ClassSelect>
  );
}
