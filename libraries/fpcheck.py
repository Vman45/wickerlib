# Scan all parts and build a Markdown table list
# Create a README file in the footprint library directory
# Table looks like this:
# |Footprint|Verified|

import os, glob, datetime

# collect a list of all module names

fplibdir = "/home/wicker/wickerlib/libraries/Wickerlib.pretty/"
modules = glob.glob(fplibdir+'*.kicad_mod')
modules = sorted(modules)

for fp in modules:
  fp = fp.replace("/home/wicker/wickerlib/libraries/Wickerlib.pretty/","")
  fp = fp.replace(".kicad_mod","")
  #print fp

# collect a list of all the symbol names

symlibfile = "/home/wicker/wickerlib/libraries/wickerlib.lib"
symlist = []

with open(symlibfile, 'r') as symfile:
  for line in  symfile: 
    if 'ENDDEF' not in line:
      if 'DEF ' in line:
        m_def = '' 
        m_fp = ''
        m_def = line.split(' ')[1]
      if 'F2 ' in line:
        m_fp = line.split(' ')[1].replace("\"","")
        if m_fp != '':
          symlist.append((m_def,m_fp))
      
for sym in symlist:

  if 'Wickerlib' not in sym[1]:
    print sym[0]+'            '+sym[1]

## search all files in the glob for the verified status
#
#for module_path in modules:
#  with open(module_path, 'r') as module:
#    for line in module:
#      if 'Verified' in line:
#        line_verify = line.lstrip('# Verified: ').rstrip('\n')
#      if 'Finished' in line:
#        line_finish = line.lstrip('# Finished: ').rstrip('\n')
#    mod_name = module_path.lstrip(libdir).rstrip('.kicad_mod')
#    liblist_output.append('| '+mod_name+' | '+line_verify+' | '+line_finish+' |')
#
#outfile_path = 'README.md'
#today = datetime.datetime.today()
#dt = today.strftime("%d %B %Y")
#
#with open(outfile_path,'w') as o:
#  o.write("# Wickerlib.pretty KiCad Module (Footprint) Library")
#  o.write("\nThese modules have been edited to have fabrication information for wickerlib. They all come with comments in the headers of each that includes attribution, the appropriate license, and whether the footprint has been used successfully in a project.")
#  o.write("\nIt is always the end user's responsibility to verify the package.")
#  o.write("\n\nThis list is updated each time the repository is updated.")
#  o.write("\n\nLast updated: "+dt)
#  o.write("\n\n|Module Name|Verified|Finished|")
#  o.write("\n|------|--------|--------|")
#  for l in liblist_output:
#    o.write("\n"+l)
