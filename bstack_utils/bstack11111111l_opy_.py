# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11l1llll1l1_opy_, bstack1111l1111_opy_, bstack1l1l1ll1_opy_, bstack1l111ll1l_opy_, \
    bstack11l1lllll11_opy_
from bstack_utils.measure import measure
def bstack1lll1l1111_opy_(bstack11l1llll11l_opy_):
    for driver in bstack11l1llll11l_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11l1l1l1ll_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
def bstack11l1l111ll_opy_(driver, status, reason=bstack11ll1ll_opy_ (u"ࠬ࠭᜵")):
    bstack1llllll1l_opy_ = Config.bstack1lll11ll1_opy_()
    if bstack1llllll1l_opy_.bstack111111l1_opy_():
        return
    bstack11l1l1l11_opy_ = bstack11ll1111l1_opy_(bstack11ll1ll_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩ᜶"), bstack11ll1ll_opy_ (u"ࠧࠨ᜷"), status, reason, bstack11ll1ll_opy_ (u"ࠨࠩ᜸"), bstack11ll1ll_opy_ (u"ࠩࠪ᜹"))
    driver.execute_script(bstack11l1l1l11_opy_)
@measure(event_name=EVENTS.bstack11l1l1l1ll_opy_, stage=STAGE.bstack11l11ll1ll_opy_)
def bstack1lll111ll1_opy_(page, status, reason=bstack11ll1ll_opy_ (u"ࠪࠫ᜺")):
    try:
        if page is None:
            return
        bstack1llllll1l_opy_ = Config.bstack1lll11ll1_opy_()
        if bstack1llllll1l_opy_.bstack111111l1_opy_():
            return
        bstack11l1l1l11_opy_ = bstack11ll1111l1_opy_(bstack11ll1ll_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧ᜻"), bstack11ll1ll_opy_ (u"ࠬ࠭᜼"), status, reason, bstack11ll1ll_opy_ (u"࠭ࠧ᜽"), bstack11ll1ll_opy_ (u"ࠧࠨ᜾"))
        page.evaluate(bstack11ll1ll_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤ᜿"), bstack11l1l1l11_opy_)
    except Exception as e:
        print(bstack11ll1ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡸࡹ࡯࡮ࡨࠢࡶࡩࡸࡹࡩࡰࡰࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࢀࢃࠢᝀ"), e)
def bstack11ll1111l1_opy_(type, name, status, reason, bstack111llll11l_opy_, bstack11ll11ll1_opy_):
    bstack1ll1l1ll11_opy_ = {
        bstack11ll1ll_opy_ (u"ࠪࡥࡨࡺࡩࡰࡰࠪᝁ"): type,
        bstack11ll1ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᝂ"): {}
    }
    if type == bstack11ll1ll_opy_ (u"ࠬࡧ࡮࡯ࡱࡷࡥࡹ࡫ࠧᝃ"):
        bstack1ll1l1ll11_opy_[bstack11ll1ll_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᝄ")][bstack11ll1ll_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭ᝅ")] = bstack111llll11l_opy_
        bstack1ll1l1ll11_opy_[bstack11ll1ll_opy_ (u"ࠨࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠫᝆ")][bstack11ll1ll_opy_ (u"ࠩࡧࡥࡹࡧࠧᝇ")] = json.dumps(str(bstack11ll11ll1_opy_))
    if type == bstack11ll1ll_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠫᝈ"):
        bstack1ll1l1ll11_opy_[bstack11ll1ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᝉ")][bstack11ll1ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪᝊ")] = name
    if type == bstack11ll1ll_opy_ (u"࠭ࡳࡦࡶࡖࡩࡸࡹࡩࡰࡰࡖࡸࡦࡺࡵࡴࠩᝋ"):
        bstack1ll1l1ll11_opy_[bstack11ll1ll_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᝌ")][bstack11ll1ll_opy_ (u"ࠨࡵࡷࡥࡹࡻࡳࠨᝍ")] = status
        if status == bstack11ll1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᝎ") and str(reason) != bstack11ll1ll_opy_ (u"ࠥࠦᝏ"):
            bstack1ll1l1ll11_opy_[bstack11ll1ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹࠧᝐ")][bstack11ll1ll_opy_ (u"ࠬࡸࡥࡢࡵࡲࡲࠬᝑ")] = json.dumps(str(reason))
    bstack11l1ll1lll_opy_ = bstack11ll1ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫᝒ").format(json.dumps(bstack1ll1l1ll11_opy_))
    return bstack11l1ll1lll_opy_
def bstack1llll1lll1_opy_(url, config, logger, bstack1l1111ll11_opy_=False):
    hostname = bstack1111l1111_opy_(url)
    is_private = bstack1l111ll1l_opy_(hostname)
    try:
        if is_private or bstack1l1111ll11_opy_:
            file_path = bstack11l1llll1l1_opy_(bstack11ll1ll_opy_ (u"ࠧ࠯ࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠧᝓ"), bstack11ll1ll_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧ᝔"), logger)
            if os.environ.get(bstack11ll1ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧ᝕")) and eval(
                    os.environ.get(bstack11ll1ll_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡏࡓࡈࡇࡌࡠࡐࡒࡘࡤ࡙ࡅࡕࡡࡈࡖࡗࡕࡒࠨ᝖"))):
                return
            if (bstack11ll1ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ᝗") in config and not config[bstack11ll1ll_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡐࡴࡩࡡ࡭ࠩ᝘")]):
                os.environ[bstack11ll1ll_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡒࡏࡄࡃࡏࡣࡓࡕࡔࡠࡕࡈࡘࡤࡋࡒࡓࡑࡕࠫ᝙")] = str(True)
                bstack11l1llll1ll_opy_ = {bstack11ll1ll_opy_ (u"ࠧࡩࡱࡶࡸࡳࡧ࡭ࡦࠩ᝚"): hostname}
                bstack11l1lllll11_opy_(bstack11ll1ll_opy_ (u"ࠨ࠰ࡥࡷࡹࡧࡣ࡬࠯ࡦࡳࡳ࡬ࡩࡨ࠰࡭ࡷࡴࡴࠧ᝛"), bstack11ll1ll_opy_ (u"ࠩࡱࡹࡩ࡭ࡥࡠ࡮ࡲࡧࡦࡲࠧ᝜"), bstack11l1llll1ll_opy_, logger)
    except Exception as e:
        pass
def bstack1l1l1l11l1_opy_(caps, bstack11l1lllllll_opy_):
    if bstack11ll1ll_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ᝝") in caps:
        caps[bstack11ll1ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬ᝞")][bstack11ll1ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࠫ᝟")] = True
        if bstack11l1lllllll_opy_:
            caps[bstack11ll1ll_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰࡀ࡯ࡱࡶ࡬ࡳࡳࡹࠧᝠ")][bstack11ll1ll_opy_ (u"ࠧ࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᝡ")] = bstack11l1lllllll_opy_
    else:
        caps[bstack11ll1ll_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱ࠭ᝢ")] = True
        if bstack11l1lllllll_opy_:
            caps[bstack11ll1ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫࠯࡮ࡲࡧࡦࡲࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠪᝣ")] = bstack11l1lllllll_opy_
def bstack11l1llllll1_opy_(bstack1l1l1l11_opy_):
    bstack11l1lllll1l_opy_ = bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡔࡶࡤࡸࡺࡹࠧᝤ"), bstack11ll1ll_opy_ (u"ࠫࠬᝥ"))
    if bstack11l1lllll1l_opy_ == bstack11ll1ll_opy_ (u"ࠬ࠭ᝦ") or bstack11l1lllll1l_opy_ == bstack11ll1ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᝧ"):
        threading.current_thread().testStatus = bstack1l1l1l11_opy_
    else:
        if bstack1l1l1l11_opy_ == bstack11ll1ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᝨ"):
            threading.current_thread().testStatus = bstack1l1l1l11_opy_