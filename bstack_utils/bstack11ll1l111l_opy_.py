# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import json
import os
import threading
from bstack_utils.config import Config
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.helper import bstack11l1llll1ll_opy_, bstack11ll11lll_opy_, bstack1llll11l_opy_, bstack11ll1ll11_opy_, \
    bstack11l1lllll11_opy_
from bstack_utils.measure import measure
def bstack1l111111ll_opy_(bstack11l1llllll1_opy_):
    for driver in bstack11l1llllll1_opy_:
        try:
            driver.quit()
        except Exception as e:
            pass
@measure(event_name=EVENTS.bstack1ll11l11ll_opy_, stage=STAGE.bstack1111ll111_opy_)
def bstack1llll1l111_opy_(driver, status, reason=bstack11l1111_opy_ (u"᜴ࠫࠬ")):
    bstack1llll11ll_opy_ = Config.bstack1llllllll_opy_()
    if bstack1llll11ll_opy_.bstack111ll1l1_opy_():
        return
    bstack1ll11l111_opy_ = bstack1l11ll11l_opy_(bstack11l1111_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨ᜵"), bstack11l1111_opy_ (u"࠭ࠧ᜶"), status, reason, bstack11l1111_opy_ (u"ࠧࠨ᜷"), bstack11l1111_opy_ (u"ࠨࠩ᜸"))
    driver.execute_script(bstack1ll11l111_opy_)
@measure(event_name=EVENTS.bstack1ll11l11ll_opy_, stage=STAGE.bstack1111ll111_opy_)
def bstack11l1ll11l_opy_(page, status, reason=bstack11l1111_opy_ (u"ࠩࠪ᜹")):
    try:
        if page is None:
            return
        bstack1llll11ll_opy_ = Config.bstack1llllllll_opy_()
        if bstack1llll11ll_opy_.bstack111ll1l1_opy_():
            return
        bstack1ll11l111_opy_ = bstack1l11ll11l_opy_(bstack11l1111_opy_ (u"ࠪࡷࡪࡺࡓࡦࡵࡶ࡭ࡴࡴࡓࡵࡣࡷࡹࡸ࠭᜺"), bstack11l1111_opy_ (u"ࠫࠬ᜻"), status, reason, bstack11l1111_opy_ (u"ࠬ࠭᜼"), bstack11l1111_opy_ (u"࠭ࠧ᜽"))
        page.evaluate(bstack11l1111_opy_ (u"ࠢࡠࠢࡀࡂࠥࢁࡽࠣ᜾"), bstack1ll11l111_opy_)
    except Exception as e:
        print(bstack11l1111_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡷࡸ࡮ࡴࡧࠡࡵࡨࡷࡸ࡯࡯࡯ࠢࡶࡸࡦࡺࡵࡴࠢࡩࡳࡷࠦࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠣࡿࢂࠨ᜿"), e)
def bstack1l11ll11l_opy_(type, name, status, reason, bstack111lll1l1_opy_, bstack1l1llll1ll_opy_):
    bstack111l111ll1_opy_ = {
        bstack11l1111_opy_ (u"ࠩࡤࡧࡹ࡯࡯࡯ࠩᝀ"): type,
        bstack11l1111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᝁ"): {}
    }
    if type == bstack11l1111_opy_ (u"ࠫࡦࡴ࡮ࡰࡶࡤࡸࡪ࠭ᝂ"):
        bstack111l111ll1_opy_[bstack11l1111_opy_ (u"ࠬࡧࡲࡨࡷࡰࡩࡳࡺࡳࠨᝃ")][bstack11l1111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᝄ")] = bstack111lll1l1_opy_
        bstack111l111ll1_opy_[bstack11l1111_opy_ (u"ࠧࡢࡴࡪࡹࡲ࡫࡮ࡵࡵࠪᝅ")][bstack11l1111_opy_ (u"ࠨࡦࡤࡸࡦ࠭ᝆ")] = json.dumps(str(bstack1l1llll1ll_opy_))
    if type == bstack11l1111_opy_ (u"ࠩࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳࡔࡡ࡮ࡧࠪᝇ"):
        bstack111l111ll1_opy_[bstack11l1111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᝈ")][bstack11l1111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᝉ")] = name
    if type == bstack11l1111_opy_ (u"ࠬࡹࡥࡵࡕࡨࡷࡸ࡯࡯࡯ࡕࡷࡥࡹࡻࡳࠨᝊ"):
        bstack111l111ll1_opy_[bstack11l1111_opy_ (u"࠭ࡡࡳࡩࡸࡱࡪࡴࡴࡴࠩᝋ")][bstack11l1111_opy_ (u"ࠧࡴࡶࡤࡸࡺࡹࠧᝌ")] = status
        if status == bstack11l1111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᝍ") and str(reason) != bstack11l1111_opy_ (u"ࠤࠥᝎ"):
            bstack111l111ll1_opy_[bstack11l1111_opy_ (u"ࠪࡥࡷ࡭ࡵ࡮ࡧࡱࡸࡸ࠭ᝏ")][bstack11l1111_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᝐ")] = json.dumps(str(reason))
    bstack1111l111l1_opy_ = bstack11l1111_opy_ (u"ࠬࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࡣࡪࡾࡥࡤࡷࡷࡳࡷࡀࠠࡼࡿࠪᝑ").format(json.dumps(bstack111l111ll1_opy_))
    return bstack1111l111l1_opy_
def bstack1l1llll11_opy_(url, config, logger, bstack11l11l1111_opy_=False):
    hostname = bstack11ll11lll_opy_(url)
    is_private = bstack11ll1ll11_opy_(hostname)
    try:
        if is_private or bstack11l11l1111_opy_:
            file_path = bstack11l1llll1ll_opy_(bstack11l1111_opy_ (u"࠭࠮ࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠭ᝒ"), bstack11l1111_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭ᝓ"), logger)
            if os.environ.get(bstack11l1111_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡍࡑࡆࡅࡑࡥࡎࡐࡖࡢࡗࡊ࡚࡟ࡆࡔࡕࡓࡗ࠭᝔")) and eval(
                    os.environ.get(bstack11l1111_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡎࡒࡇࡆࡒ࡟ࡏࡑࡗࡣࡘࡋࡔࡠࡇࡕࡖࡔࡘࠧ᝕"))):
                return
            if (bstack11l1111_opy_ (u"ࠪࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡎࡲࡧࡦࡲࠧ᝖") in config and not config[bstack11l1111_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡏࡳࡨࡧ࡬ࠨ᝗")]):
                os.environ[bstack11l1111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡑࡕࡃࡂࡎࡢࡒࡔ࡚࡟ࡔࡇࡗࡣࡊࡘࡒࡐࡔࠪ᝘")] = str(True)
                bstack11l1lllll1l_opy_ = {bstack11l1111_opy_ (u"࠭ࡨࡰࡵࡷࡲࡦࡳࡥࠨ᝙"): hostname}
                bstack11l1lllll11_opy_(bstack11l1111_opy_ (u"ࠧ࠯ࡤࡶࡸࡦࡩ࡫࠮ࡥࡲࡲ࡫࡯ࡧ࠯࡬ࡶࡳࡳ࠭᝚"), bstack11l1111_opy_ (u"ࠨࡰࡸࡨ࡬࡫࡟࡭ࡱࡦࡥࡱ࠭᝛"), bstack11l1lllll1l_opy_, logger)
    except Exception as e:
        pass
def bstack111l1l111_opy_(caps, bstack11l1lllllll_opy_):
    if bstack11l1111_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬࠼ࡲࡴࡹ࡯࡯࡯ࡵࠪ᝜") in caps:
        caps[bstack11l1111_opy_ (u"ࠪࡦࡸࡺࡡࡤ࡭࠽ࡳࡵࡺࡩࡰࡰࡶࠫ᝝")][bstack11l1111_opy_ (u"ࠫࡱࡵࡣࡢ࡮ࠪ᝞")] = True
        if bstack11l1lllllll_opy_:
            caps[bstack11l1111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯࠿ࡵࡰࡵ࡫ࡲࡲࡸ࠭᝟")][bstack11l1111_opy_ (u"࠭࡬ࡰࡥࡤࡰࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠨᝠ")] = bstack11l1lllllll_opy_
    else:
        caps[bstack11l1111_opy_ (u"ࠧࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰ࠴࡬ࡰࡥࡤࡰࠬᝡ")] = True
        if bstack11l1lllllll_opy_:
            caps[bstack11l1111_opy_ (u"ࠨࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱ࠮࡭ࡱࡦࡥࡱࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠩᝢ")] = bstack11l1lllllll_opy_
def bstack11l1llll11l_opy_(bstack1lll11l1_opy_):
    bstack11l1llll1l1_opy_ = bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠩࡷࡩࡸࡺࡓࡵࡣࡷࡹࡸ࠭ᝣ"), bstack11l1111_opy_ (u"ࠪࠫᝤ"))
    if bstack11l1llll1l1_opy_ == bstack11l1111_opy_ (u"ࠫࠬᝥ") or bstack11l1llll1l1_opy_ == bstack11l1111_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᝦ"):
        threading.current_thread().testStatus = bstack1lll11l1_opy_
    else:
        if bstack1lll11l1_opy_ == bstack11l1111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᝧ"):
            threading.current_thread().testStatus = bstack1lll11l1_opy_