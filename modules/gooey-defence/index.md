---
posttype: "module"
title: "Gooey Defence"
cover: "../../static/logos/cover.jpg"
date: "01/01/2017"
category: "tech"
tags: ["Gameplay Template"]
---
This module serves as the main module for the Gooey's Defence Gameplay Template.  
It currently is undergoing active development and thus is not at a public release stage.

## How To Play (at the moment)
Currently this modules lacks a few features that make it publicly playable. However it does have many feature currently implemented. As such this shall outline all the current features and how to use them.

#### Activation 
Firstly, please start a new world after updating this module. During development I shall make no guarantees that the module will be backwards compatible.  
Once your new world has loaded you will need to activate it. That is currently done by simply interacting with any block via `E`.

If the world loaded correctly you should see translucent blue lines crossing the field from the entrances to the shrine. These are the paths the enemies will take in order to reach the spawn. As you alter the world, the paths will also change. If no path is found then the blue line will disappear and your game will probably crash at the moment.  
Likewise be careful using the debugger, if the pathfinding times out (and it does count time paused in the debugger) then your game will crash.  
Probably.


#### Enemies
In order to spawn in some enemies just interact with the world again. This can be via the `E` key or by using an item you are holding with `right click`. This does include placing blocks, so do with that as you will.

There are three enemy types at the moment, `BasicEnemy`, `FastEnemy` and `StrongEnemy`. However in order to spawn in different types you will need to edit the `EnemyManager#spawnEnemy()` method. Simply change the prefab referenced to one of the other types and recompile.  

When an enemy reaches the shrine, it will be destroyed and make the shrine flash red briefly. The game will not end, so don't worry about having your testing constantly interrupted.

#### Towers
The last bit of information you need at the moment is the towers. These are the multiblock structures that will attack the enemies and damage them, with the enemies eventually dying if they reach zero health.

A tower is made up of at least three blocks.  
The first block type is **Cores**. These provide power to the other blocks, so make sure that you have enough cores to provide power to the tower.  

The second block type is **Targeters**. These are the blocks that actually attack the enemies. There are a number of different Targeter blocks, all with different strengths and weaknesses. They are listed below.  
Crucially, Targeters don't need to actually see the enemy to shoot it, with their shots phasing through blocks. You can also stack multiple different types of Targeters onto a single tower. For now...

Lastly you have **Effectors**. Although Targeters attack the enemies, their shots won't actually do anything. Effectors provide an effect to the enemies that are targeted.  
The effects range from damage, to crowd control to both. Like the Targeters, multiple types can be stacked onto a single tower to apply multiple different effects. This does mean that you can technically freeze and ignite an enemy at the same time. Which is why multiple effect stacking will probably be tweaked in future. Abuse it before you lose it.

**Plain** blocks are the odd type out. They provide no function to the tower, but they allow the blocks to connect without having to directly touch. They are useful if you want to connect some of the above blocks but don't actually want to have to use a more expensive functional block to do so.

#### Upgrading
If you want to upgrade the effectiveness of the tower's blocks you can. By interacting with a tower via `E` you can bring up the tower screen. This has a list of all the targeters and effectors in the tower. By selecting one you can view the details of that block and upgrade it. A block can be upgraded in multiple different ways. You can always upgrade the range and attack speed but some other towers have other upgrades you can buy.  
If you break an upgraded block you will lose all your upgrades and have to re apply them. This is only a minor inconvenience at the moment, but when upgrades start to cost money will become more serious. The costs will also not be refunded. You break it, you pay for it.