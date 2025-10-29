# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll1111l11_opy_, bstack111l1l11l_opy_, bstack1l11l111_opy_, bstack1111lll11l_opy_, \
    bstack11ll11111ll_opy_
from bstack_utils.measure import measure
def bstack1llllll1l1_opy_(bstack11ll11111l1_opy_):
    for driver in bstack11ll11111l1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack11111ll11l_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
def bstack111l1l11l1_opy_(driver, status, reason=bstack11l11ll_opy_ (u"ࠪࠫᜥ")):
    bstack1lll11111_opy_ = Config.bstack1llll111l_opy_()
    if bstack1lll11111_opy_.bstack1lllllll1_opy_():
        return
    bstack11ll11l111_opy_ = bstack1l111111l1_opy_(bstack11l11ll_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᜦ"), bstack11l11ll_opy_ (u"ࠬ࠭ᜧ"), status, reason, bstack11l11ll_opy_ (u"࠭ࠧᜨ"), bstack11l11ll_opy_ (u"ࠧࠨᜩ"))
    driver.execute_script(bstack11ll11l111_opy_)
@measure(event_name=EVENTS.bstack11111ll11l_opy_, stage=STAGE.bstack1l1l1l1lll_opy_)
def bstack1ll111l1l1_opy_(page, status, reason=bstack11l11ll_opy_ (u"ࠨࠩᜪ")):
    try:
        if page is None:
            return
        bstack1lll11111_opy_ = Config.bstack1llll111l_opy_()
        if bstack1lll11111_opy_.bstack1lllllll1_opy_():
            return
        bstack11ll11l111_opy_ = bstack1l111111l1_opy_(bstack11l11ll_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᜫ"), bstack11l11ll_opy_ (u"ࠪࠫᜬ"), status, reason, bstack11l11ll_opy_ (u"ࠫࠬᜭ"), bstack11l11ll_opy_ (u"ࠬ࠭ᜮ"))
        page.evaluate(bstack11l11ll_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᜯ"), bstack11ll11l111_opy_)
    except Exception as e:
        print(bstack11l11ll_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡾࢁࠧᜰ"), e)
def bstack1l111111l1_opy_(type, name, status, reason, bstack1111l1ll1l_opy_, bstack111ll1llll_opy_):
    bstack11l111ll1_opy_ = {
        bstack11l11ll_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨᜱ"): type,
        bstack11l11ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᜲ"): {}
    }
    if type == bstack11l11ll_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬᜳ"):
        bstack11l111ll1_opy_[bstack11l11ll_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹ᜴ࠧ")][bstack11l11ll_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ᜵")] = bstack1111l1ll1l_opy_
        bstack11l111ll1_opy_[bstack11l11ll_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ᜶")][bstack11l11ll_opy_ (u"ࠧࡥࡣࡷࡥࠬ᜷")] = json.dumps(str(bstack111ll1llll_opy_))
    if type == bstack11l11ll_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ᜸"):
        bstack11l111ll1_opy_[bstack11l11ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ᜹")][bstack11l11ll_opy_ (u"ࠪࡲࡦࡳࡥࠨ᜺")] = name
    if type == bstack11l11ll_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧ᜻"):
        bstack11l111ll1_opy_[bstack11l11ll_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ᜼")][bstack11l11ll_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭᜽")] = status
        if status == bstack11l11ll_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ᜾") and str(reason) != bstack11l11ll_opy_ (u"ࠣࠤ᜿"):
            bstack11l111ll1_opy_[bstack11l11ll_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᝀ")][bstack11l11ll_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪᝁ")] = json.dumps(str(reason))
    bstack111111ll11_opy_ = bstack11l11ll_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩᝂ").format(json.dumps(bstack11l111ll1_opy_))
    return bstack111111ll11_opy_
def bstack1l111l1lll_opy_(url, config, logger, bstack1l1111llll_opy_=False):
    hostname = bstack111l1l11l_opy_(url)
    is_private = bstack1111lll11l_opy_(hostname)
    try:
        if is_private or bstack1l1111llll_opy_:
            file_path = bstack11ll1111l11_opy_(bstack11l11ll_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᝃ"), bstack11l11ll_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬᝄ"), logger)
            if os.environ.get(bstack11l11ll_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬᝅ")) and eval(
                    os.environ.get(bstack11l11ll_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ᝆ"))):
                return
            if (bstack11l11ll_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᝇ") in config and not config[bstack11l11ll_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᝈ")]):
                os.environ[bstack11l11ll_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩᝉ")] = str(True)
                bstack11ll1111111_opy_ = {bstack11l11ll_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧᝊ"): hostname}
                bstack11ll11111ll_opy_(bstack11l11ll_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬᝋ"), bstack11l11ll_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬᝌ"), bstack11ll1111111_opy_, logger)
    except Exception as e:
        pass
def bstack1ll1l111l_opy_(caps, bstack11l1llllll1_opy_):
    if bstack11l11ll_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᝍ") in caps:
        caps[bstack11l11ll_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᝎ")][bstack11l11ll_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩᝏ")] = True
        if bstack11l1llllll1_opy_:
            caps[bstack11l11ll_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᝐ")][bstack11l11ll_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᝑ")] = bstack11l1llllll1_opy_
    else:
        caps[bstack11l11ll_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫᝒ")] = True
        if bstack11l1llllll1_opy_:
            caps[bstack11l11ll_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᝓ")] = bstack11l1llllll1_opy_
def bstack11ll111111l_opy_(bstack1l1111ll_opy_):
    bstack11l1lllllll_opy_ = bstack1l11l111_opy_(threading.current_thread(), bstack11l11ll_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬ᝔"), bstack11l11ll_opy_ (u"ࠩࠪ᝕"))
    if bstack11l1lllllll_opy_ == bstack11l11ll_opy_ (u"ࠪࠫ᝖") or bstack11l1lllllll_opy_ == bstack11l11ll_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ᝗"):
        threading.current_thread().testStatus = bstack1l1111ll_opy_
    else:
        if bstack1l1111ll_opy_ == bstack11l11ll_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ᝘"):
            threading.current_thread().testStatus = bstack1l1111ll_opy_