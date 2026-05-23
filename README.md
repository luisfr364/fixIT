# fixIT ⚙️

Fixit is a program made to solve simple IT problems easily with a just few clicks. 




## Routing
- The routing system used is a simple state-based routing.
- The state variable is defined on `main_window.slint` and is used to determine which page to show.
- The function used to change the state is `navigate_to()` which is defined in `main_window.slint`
- 

## Folder Structure
├───components
│   ├───monitoring_page
│   ├───shared
│   ├───support_page
│   └───welcome_page
├───controllers
├───helpers
├───pages
├───public
│   └───images
├───scripts

### Components Folder 📁
- Contains all the components used in one or more pages.
- Each component is inside a subfolder with the name of the page where it is used.
- Components that are used inside one or more pages are inside tha `shared` folder.
