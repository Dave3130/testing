# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11ll1111111_opy_, bstack111ll1l1l1_opy_, bstack1lllll11_opy_, bstack11l1l1l11_opy_, \
    bstack11ll11111l1_opy_
from bstack_utils.measure import measure
def bstack111l1ll11l_opy_(bstack11l1llllll1_opy_):
    for driver in bstack11l1llllll1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1ll1ll111l_opy_, stage=STAGE.bstack11ll11lll_opy_)
def bstack1l11ll11l1_opy_(driver, status, reason=bstack11ll1l_opy_ (u"ࠪࠫᜥ")):
    bstack111ll1l1_opy_ = Config.bstack111111ll_opy_()
    if bstack111ll1l1_opy_.bstack1lll1lll1_opy_():
        return
    bstack1111l1l111_opy_ = bstack1l1ll1llll_opy_(bstack11ll1l_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧᜦ"), bstack11ll1l_opy_ (u"ࠬ࠭ᜧ"), status, reason, bstack11ll1l_opy_ (u"࠭ࠧᜨ"), bstack11ll1l_opy_ (u"ࠧࠨᜩ"))
    driver.execute_script(bstack1111l1l111_opy_)
@measure(event_name=EVENTS.bstack1ll1ll111l_opy_, stage=STAGE.bstack11ll11lll_opy_)
def bstack1l1111l11_opy_(page, status, reason=bstack11ll1l_opy_ (u"ࠨࠩᜪ")):
    try:
        if page is None:
            return
        bstack111ll1l1_opy_ = Config.bstack111111ll_opy_()
        if bstack111ll1l1_opy_.bstack1lll1lll1_opy_():
            return
        bstack1111l1l111_opy_ = bstack1l1ll1llll_opy_(bstack11ll1l_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠬᜫ"), bstack11ll1l_opy_ (u"ࠪࠫᜬ"), status, reason, bstack11ll1l_opy_ (u"ࠫࠬᜭ"), bstack11ll1l_opy_ (u"ࠬ࠭ᜮ"))
        page.evaluate(bstack11ll1l_opy_ (u"ࠨ࡟ࠡ࠿ࡁࠤࢀࢃࠢᜯ"), bstack1111l1l111_opy_)
    except Exception as e:
        print(bstack11ll1l_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡶࡷ࡭ࡳ࡭ࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡࡨࡲࡶࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡾࢁࠧᜰ"), e)
def bstack1l1ll1llll_opy_(type, name, status, reason, bstack1ll1llll11_opy_, bstack111l1lll1l_opy_):
    bstack1l1l11l11l_opy_ = {
        bstack11ll1l_opy_ (u"ࠨࡣࡦࡸ࡮ࡵ࡮ࠨᜱ"): type,
        bstack11ll1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᜲ"): {}
    }
    if type == bstack11ll1l_opy_ (u"ࠪࡥࡳࡴ࡯ࡵࡣࡷࡩࠬᜳ"):
        bstack1l1l11l11l_opy_[bstack11ll1l_opy_ (u"ࠫࡦࡸࡧࡶ࡯ࡨࡲࡹࡹ᜴ࠧ")][bstack11ll1l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ᜵")] = bstack1ll1llll11_opy_
        bstack1l1l11l11l_opy_[bstack11ll1l_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩ᜶")][bstack11ll1l_opy_ (u"ࠧࡥࡣࡷࡥࠬ᜷")] = json.dumps(str(bstack111l1lll1l_opy_))
    if type == bstack11ll1l_opy_ (u"ࠨࡵࡨࡸࡘ࡫ࡳࡴ࡫ࡲࡲࡓࡧ࡭ࡦࠩ᜸"):
        bstack1l1l11l11l_opy_[bstack11ll1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬ᜹")][bstack11ll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨ᜺")] = name
    if type == bstack11ll1l_opy_ (u"ࠫࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡔࡶࡤࡸࡺࡹࠧ᜻"):
        bstack1l1l11l11l_opy_[bstack11ll1l_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨ᜼")][bstack11ll1l_opy_ (u"࠭ࡳࡵࡣࡷࡹࡸ࠭᜽")] = status
        if status == bstack11ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ᜾") and str(reason) != bstack11ll1l_opy_ (u"ࠣࠤ᜿"):
            bstack1l1l11l11l_opy_[bstack11ll1l_opy_ (u"ࠩࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠬᝀ")][bstack11ll1l_opy_ (u"ࠪࡶࡪࡧࡳࡰࡰࠪᝁ")] = json.dumps(str(reason))
    bstack1111111l1l_opy_ = bstack11ll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࡾࠩᝂ").format(json.dumps(bstack1l1l11l11l_opy_))
    return bstack1111111l1l_opy_
def bstack1l1l11l1l1_opy_(url, config, logger, bstack1111lll1ll_opy_=False):
    hostname = bstack111ll1l1l1_opy_(url)
    is_private = bstack11l1l1l11_opy_(hostname)
    try:
        if is_private or bstack1111lll1ll_opy_:
            file_path = bstack11ll1111111_opy_(bstack11ll1l_opy_ (u"ࠬ࠴ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠬᝃ"), bstack11ll1l_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬᝄ"), logger)
            if os.environ.get(bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡌࡐࡅࡄࡐࡤࡔࡏࡕࡡࡖࡉ࡙ࡥࡅࡓࡔࡒࡖࠬᝅ")) and eval(
                    os.environ.get(bstack11ll1l_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭ᝆ"))):
                return
            if (bstack11ll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡍࡱࡦࡥࡱ࠭ᝇ") in config and not config[bstack11ll1l_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧᝈ")]):
                os.environ[bstack11ll1l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡐࡔࡉࡁࡍࡡࡑࡓ࡙ࡥࡓࡆࡖࡢࡉࡗࡘࡏࡓࠩᝉ")] = str(True)
                bstack11l1lllllll_opy_ = {bstack11ll1l_opy_ (u"ࠬ࡮࡯ࡴࡶࡱࡥࡲ࡫ࠧᝊ"): hostname}
                bstack11ll11111l1_opy_(bstack11ll1l_opy_ (u"࠭࠮ࡣࡵࡷࡥࡨࡱ࠭ࡤࡱࡱࡪ࡮࡭࠮࡫ࡵࡲࡲࠬᝋ"), bstack11ll1l_opy_ (u"ࠧ࡯ࡷࡧ࡫ࡪࡥ࡬ࡰࡥࡤࡰࠬᝌ"), bstack11l1lllllll_opy_, logger)
    except Exception as e:
        pass
def bstack1l111l11ll_opy_(caps, bstack11ll111111l_opy_):
    if bstack11ll1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫࠻ࡱࡳࡸ࡮ࡵ࡮ࡴࠩᝍ") in caps:
        caps[bstack11ll1l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪᝎ")][bstack11ll1l_opy_ (u"ࠪࡰࡴࡩࡡ࡭ࠩᝏ")] = True
        if bstack11ll111111l_opy_:
            caps[bstack11ll1l_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮࠾ࡴࡶࡴࡪࡱࡱࡷࠬᝐ")][bstack11ll1l_opy_ (u"ࠬࡲ࡯ࡤࡣ࡯ࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠧᝑ")] = bstack11ll111111l_opy_
    else:
        caps[bstack11ll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯࠳ࡲ࡯ࡤࡣ࡯ࠫᝒ")] = True
        if bstack11ll111111l_opy_:
            caps[bstack11ll1l_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᝓ")] = bstack11ll111111l_opy_
def bstack11ll11111ll_opy_(bstack1l1lllll_opy_):
    bstack11ll1111l11_opy_ = bstack1lllll11_opy_(threading.current_thread(), bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹ࡙ࡴࡢࡶࡸࡷࠬ᝔"), bstack11ll1l_opy_ (u"ࠩࠪ᝕"))
    if bstack11ll1111l11_opy_ == bstack11ll1l_opy_ (u"ࠪࠫ᝖") or bstack11ll1111l11_opy_ == bstack11ll1l_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ᝗"):
        threading.current_thread().testStatus = bstack1l1lllll_opy_
    else:
        if bstack1l1lllll_opy_ == bstack11ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬ᝘"):
            threading.current_thread().testStatus = bstack1l1lllll_opy_