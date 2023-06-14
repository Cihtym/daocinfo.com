"use client";

import { Popover, Button, Text, Grid } from "@nextui-org/react";

export default function EquipmentCard({itemSlot}) {
  const placements = [
    "bottom",
  ];

  return (
    <Grid.Container gap={2} justify="center" alignContent="center">
      {placements.map((placement) => (
        <Grid key={placement}>
          <Popover placement={placement}>
            <Popover.Trigger>
              <Button size="sm" bordered color="primary" width="2rem">{itemSlot}</Button>
            </Popover.Trigger>
            <Popover.Content>
              <Text css={{ p: "$10" }}>
                This is the content of the popover.
              </Text>
            </Popover.Content>
          </Popover>
        </Grid>
      ))}
    </Grid.Container>
  );
}
