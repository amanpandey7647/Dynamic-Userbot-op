from re import findall

from search_engine_parser import GoogleSearch

from DYNAMIC import CMD_HELP
from DYNAMIC.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"gs (.*)"))
async def gsearch(q_event):
    if q_event.fwd_from:
        return
    """ For .google command, do a Google search. """
    match = q_event.pattern_match.group(1)
    page = findall(r"page=\d+", match)
    try:
        page = page[0]
        page = page.replace("page=", "")
        match = match.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(match), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    for i in range(len(gresults["links"])):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"[{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
    await q_event.edit(
        "**Search Query:**\n`" + match + "`\n\n**Results:**\n" + msg, link_preview=False
    )
