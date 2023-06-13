import React from "react";
import { Dropdown as RealmSelect } from "@nextui-org/react";

export default function App() {
  const [realm, setRealm] = React.useState(new Set(["Choose your Realm"]));

  const realmValue = React.useMemo(
    () => Array.from(realm).join(", ").replaceAll("_", " "),
    [realm]
  );

  return (
    <RealmSelect>
      <RealmSelect.Button css={{
        tt: "capitalize", 
        color: "secondary",
        borderRadius: 6,
        }}>
        {realmValue}
      </RealmSelect.Button>
      <RealmSelect.Menu
        aria-label="Single selection actions"
        color="secondary"
        disallowEmptySelection
        selectionMode="single"
        selectedKeys={realm}
        onSelectionChange={setRealm}
      >
        {/* TODO: Add images and colors to the dropdown items */}
        <RealmSelect.Item key="albion">Albion</RealmSelect.Item>
        <RealmSelect.Item key="hibernia">Hibernia</RealmSelect.Item>
        <RealmSelect.Item key="midgard">Midgard</RealmSelect.Item>
      </RealmSelect.Menu>
    </RealmSelect>
  );
}
