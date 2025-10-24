# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import os
import json
import shutil
import tempfile
import threading
import urllib.request
import uuid
from pathlib import Path
import logging
import re
from bstack_utils.helper import bstack1ll11ll1lll_opy_
bstack11lll11ll1l_opy_ = 100 * 1024 * 1024 # 100 bstack11lll111lll_opy_
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
bstack1ll1l1l1l11_opy_ = bstack1ll11ll1lll_opy_()
bstack1ll1l11l1l1_opy_ = bstack11l11l1_opy_ (u"ࠢࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠳ࠢᘦ")
bstack11llll11l1l_opy_ = bstack11l11l1_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦᘧ")
bstack11llll11ll1_opy_ = bstack11l11l1_opy_ (u"ࠤࡅࡹ࡮ࡲࡤࡍࡧࡹࡩࡱࠨᘨ")
bstack11llll111ll_opy_ = bstack11l11l1_opy_ (u"ࠥࡌࡴࡵ࡫ࡍࡧࡹࡩࡱࠨᘩ")
bstack11lll1l1l11_opy_ = bstack11l11l1_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࡉࡱࡲ࡯ࡊࡼࡥ࡯ࡶࠥᘪ")
_11lll11l1l1_opy_ = threading.local()
def bstack1ll111ll11l_opy_(test_framework_state, test_hook_state):
    bstack11l11l1_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤ࡙ࠥࡥࡵࠢࡷ࡬ࡪࠦࡣࡶࡴࡵࡩࡳࡺࠠࡵࡧࡶࡸࠥ࡫ࡶࡦࡰࡷࠤࡸࡺࡡࡵࡧࠣ࡭ࡳࠦࡴࡩࡴࡨࡥࡩ࠳࡬ࡰࡥࡤࡰࠥࡹࡴࡰࡴࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤ࡙࡮ࡩࡴࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡸ࡮࡯ࡶ࡮ࡧࠤࡧ࡫ࠠࡤࡣ࡯ࡰࡪࡪࠠࡣࡻࠣࡸ࡭࡫ࠠࡦࡸࡨࡲࡹࠦࡨࡢࡰࡧࡰࡪࡸࠠࠩࡵࡸࡧ࡭ࠦࡡࡴࠢࡷࡶࡦࡩ࡫ࡠࡧࡹࡩࡳࡺࠩࠋࠢࠣࠤࠥࡨࡥࡧࡱࡵࡩࠥࡧ࡮ࡺࠢࡩ࡭ࡱ࡫ࠠࡶࡲ࡯ࡳࡦࡪࡳࠡࡱࡦࡧࡺࡸ࠮ࠋࠢࠣࠤࠥࠨࠢࠣᘫ")
    _11lll11l1l1_opy_.test_framework_state = test_framework_state
    _11lll11l1l1_opy_.test_hook_state = test_hook_state
def bstack11lll1l1ll1_opy_():
    bstack11l11l1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡒࡦࡶࡵ࡭ࡪࡼࡥࠡࡶ࡫ࡩࠥࡩࡵࡳࡴࡨࡲࡹࠦࡴࡦࡵࡷࠤࡪࡼࡥ࡯ࡶࠣࡷࡹࡧࡴࡦࠢࡩࡶࡴࡳࠠࡵࡪࡵࡩࡦࡪ࠭࡭ࡱࡦࡥࡱࠦࡳࡵࡱࡵࡥ࡬࡫࠮ࠋࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࠦࡡࠡࡶࡸࡴࡱ࡫ࠠࠩࡶࡨࡷࡹࡥࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࡡࡶࡸࡦࡺࡥ࠭ࠢࡷࡩࡸࡺ࡟ࡩࡱࡲ࡯ࡤࡹࡴࡢࡶࡨ࠭ࠥࡵࡲࠡࠪࡑࡳࡳ࡫ࠬࠡࡐࡲࡲࡪ࠯ࠠࡪࡨࠣࡲࡴࡺࠠࡴࡧࡷ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᘬ")
    return (
        getattr(_11lll11l1l1_opy_, bstack11l11l1_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࠧᘭ"), None),
        getattr(_11lll11l1l1_opy_, bstack11l11l1_opy_ (u"ࠨࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࠪᘮ"), None)
    )
class bstack11l11l1lll_opy_:
    bstack11l11l1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡉ࡭ࡱ࡫ࡕࡱ࡮ࡲࡥࡩ࡫ࡲࠡࡲࡵࡳࡻ࡯ࡤࡦࡵࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࡦࡲࡩࡵࡻࠣࡸࡴࠦࡵࡱ࡮ࡲࡥࡩࠦࡡ࡯ࠢࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡢࡢࡵࡨࡨࠥࡵ࡮ࠡࡶ࡫ࡩࠥ࡭ࡩࡷࡧࡱࠤ࡫࡯࡬ࡦࠢࡳࡥࡹ࡮࠮ࠋࠢࠣࠤࠥࡏࡴࠡࡵࡸࡴࡵࡵࡲࡵࡵࠣࡦࡴࡺࡨࠡ࡮ࡲࡧࡦࡲࠠࡧ࡫࡯ࡩࠥࡶࡡࡵࡪࡶࠤࡦࡴࡤࠡࡊࡗࡘࡕ࠵ࡈࡕࡖࡓࡗ࡛ࠥࡒࡍࡵ࠯ࠤࡦࡴࡤࠡࡥࡲࡴ࡮࡫ࡳࠡࡶ࡫ࡩࠥ࡬ࡩ࡭ࡧࠣ࡭ࡳࡺ࡯ࠡࡣࠣࡨࡪࡹࡩࡨࡰࡤࡸࡪࡪࠊࠡࠢࠣࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿࠠࡸ࡫ࡷ࡬࡮ࡴࠠࡵࡪࡨࠤࡺࡹࡥࡳࠩࡶࠤ࡭ࡵ࡭ࡦࠢࡩࡳࡱࡪࡥࡳࠢࡸࡲࡩ࡫ࡲࠡࢀ࠲࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠲࡙ࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠰ࠍࠤࠥࠦࠠࡊࡨࠣࡥࡳࠦ࡯ࡱࡶ࡬ࡳࡳࡧ࡬ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࡶࡡࡳࡣࡰࡩࡹ࡫ࡲࠡࠪ࡬ࡲࠥࡐࡓࡐࡐࠣࡪࡴࡸ࡭ࡢࡶࠬࠤ࡮ࡹࠠࡱࡴࡲࡺ࡮ࡪࡥࡥࠢࡤࡲࡩࠦࡣࡰࡰࡷࡥ࡮ࡴࡳࠡࡣࠣࡸࡷࡻࡴࡩࡻࠣࡺࡦࡲࡵࡦࠌࠣࠤࠥࠦࡦࡰࡴࠣࡸ࡭࡫ࠠ࡬ࡧࡼࠤࠧࡨࡵࡪ࡮ࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࠢ࠭ࠢࡷ࡬ࡪࠦࡦࡪ࡮ࡨࠤࡼ࡯࡬࡭ࠢࡥࡩࠥࡶ࡬ࡢࡥࡨࡨࠥ࡯࡮ࠡࡶ࡫ࡩࠥࠨࡂࡶ࡫࡯ࡨࡑ࡫ࡶࡦ࡮ࠥࠤ࡫ࡵ࡬ࡥࡧࡵ࠿ࠥࡵࡴࡩࡧࡵࡻ࡮ࡹࡥ࠭ࠌࠣࠤࠥࠦࡩࡵࠢࡧࡩ࡫ࡧࡵ࡭ࡶࡶࠤࡹࡵࠠࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦ࠳ࠐࠠࠡࠢࠣࡘ࡭࡯ࡳࠡࡸࡨࡶࡸ࡯࡯࡯ࠢࡲࡪࠥࡧࡤࡥࡡࡤࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠦࡩࡴࠢࡤࠤࡻࡵࡩࡥࠢࡰࡩࡹ࡮࡯ࡥ⠖࡬ࡸࠥ࡮ࡡ࡯ࡦ࡯ࡩࡸࠦࡡ࡭࡮ࠣࡩࡷࡸ࡯ࡳࡵࠣ࡫ࡷࡧࡣࡦࡨࡸࡰࡱࡿࠠࡣࡻࠣࡰࡴ࡭ࡧࡪࡰࡪࠎࠥࠦࠠࠡࡶ࡫ࡩࡲࠦࡡ࡯ࡦࠣࡷ࡮ࡳࡰ࡭ࡻࠣࡶࡪࡺࡵࡳࡰ࡬ࡲ࡬ࠦࡷࡪࡶ࡫ࡳࡺࡺࠠࡵࡪࡵࡳࡼ࡯࡮ࡨࠢࡨࡼࡨ࡫ࡰࡵ࡫ࡲࡲࡸ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᘯ")
    @staticmethod
    def upload_attachment(bstack11lll1l111l_opy_: str, *bstack11lll1l11ll_opy_) -> None:
        if not bstack11lll1l111l_opy_ or not bstack11lll1l111l_opy_.strip():
            logger.error(bstack11l11l1_opy_ (u"ࠥࡥࡩࡪ࡟ࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠤ࡫ࡧࡩ࡭ࡧࡧ࠾ࠥࡖࡲࡰࡸ࡬ࡨࡪࡪࠠࡧ࡫࡯ࡩࠥࡶࡡࡵࡪࠣ࡭ࡸࠦࡥ࡮ࡲࡷࡽࠥࡵࡲࠡࡐࡲࡲࡪ࠴ࠢᘰ"))
            return
        bstack11lll11ll11_opy_ = bstack11lll1l11ll_opy_[0] if bstack11lll1l11ll_opy_ and len(bstack11lll1l11ll_opy_) > 0 else None
        bstack11lll1l1lll_opy_ = None
        test_framework_state, test_hook_state = bstack11lll1l1ll1_opy_()
        try:
            if bstack11lll1l111l_opy_.startswith(bstack11l11l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧᘱ")) or bstack11lll1l111l_opy_.startswith(bstack11l11l1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢᘲ")):
                logger.debug(bstack11l11l1_opy_ (u"ࠨࡐࡢࡶ࡫ࠤ࡮ࡹࠠࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡧࠤࡦࡹࠠࡖࡔࡏ࠿ࠥࡪ࡯ࡸࡰ࡯ࡳࡦࡪࡩ࡯ࡩࠣࡸ࡭࡫ࠠࡧ࡫࡯ࡩ࠳ࠨᘳ"))
                url = bstack11lll1l111l_opy_
                bstack11lll11l111_opy_ = str(uuid.uuid4())
                bstack11lll11l1ll_opy_ = os.path.basename(urllib.request.urlparse(url).path)
                if not bstack11lll11l1ll_opy_ or not bstack11lll11l1ll_opy_.strip():
                    bstack11lll11l1ll_opy_ = bstack11lll11l111_opy_
                temp_file = tempfile.NamedTemporaryFile(delete=False,
                                                        prefix=bstack11l11l1_opy_ (u"ࠢࡶࡲ࡯ࡳࡦࡪ࡟ࠣᘴ") + bstack11lll11l111_opy_ + bstack11l11l1_opy_ (u"ࠣࡡࠥᘵ"),
                                                        suffix=bstack11l11l1_opy_ (u"ࠤࡢࠦᘶ") + bstack11lll11l1ll_opy_)
                with urllib.request.urlopen(url) as response, open(temp_file.name, bstack11l11l1_opy_ (u"ࠪࡻࡧ࠭ᘷ")) as out_file:
                    shutil.copyfileobj(response, out_file)
                bstack11lll1l1lll_opy_ = Path(temp_file.name)
                logger.debug(bstack11l11l1_opy_ (u"ࠦࡉࡵࡷ࡯࡮ࡲࡥࡩ࡫ࡤࠡࡨ࡬ࡰࡪࠦࡴࡰࠢࡷࡩࡲࡶ࡯ࡳࡣࡵࡽࠥࡲ࡯ࡤࡣࡷ࡭ࡴࡴ࠺ࠡࡽࢀࠦᘸ").format(bstack11lll1l1lll_opy_))
            else:
                bstack11lll1l1lll_opy_ = Path(bstack11lll1l111l_opy_)
                logger.debug(bstack11l11l1_opy_ (u"ࠧࡖࡡࡵࡪࠣ࡭ࡸࠦࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡦࠣࡥࡸࠦ࡬ࡰࡥࡤࡰࠥ࡬ࡩ࡭ࡧ࠽ࠤࢀࢃࠢᘹ").format(bstack11lll1l1lll_opy_))
        except Exception as e:
            logger.error(bstack11l11l1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡲࡦࡹࡧࡩ࡯ࠢࡩ࡭ࡱ࡫ࠠࡧࡴࡲࡱࠥࡶࡡࡵࡪ࠲࡙ࡗࡒ࠺ࠡࡽࢀࠦᘺ").format(e))
            return
        if bstack11lll1l1lll_opy_ is None or not bstack11lll1l1lll_opy_.exists():
            logger.error(bstack11l11l1_opy_ (u"ࠢࡔࡱࡸࡶࡨ࡫ࠠࡧ࡫࡯ࡩࠥࡪ࡯ࡦࡵࠣࡲࡴࡺࠠࡦࡺ࡬ࡷࡹࡀࠠࡼࡿࠥᘻ").format(bstack11lll1l1lll_opy_))
            return
        if bstack11lll1l1lll_opy_.stat().st_size > bstack11lll11ll1l_opy_:
            logger.error(bstack11l11l1_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࡳࡪࡼࡨࠤࡪࡾࡣࡦࡧࡧࡷࠥࡳࡡࡹ࡫ࡰࡹࡲࠦࡡ࡭࡮ࡲࡻࡪࡪࠠࡴ࡫ࡽࡩࠥࡵࡦࠡࡽࢀࠦᘼ").format(bstack11lll11ll1l_opy_))
            return
        bstack11lll1l11l1_opy_ = bstack11l11l1_opy_ (u"ࠤࡗࡩࡸࡺࡌࡦࡸࡨࡰࠧᘽ")
        if bstack11lll11ll11_opy_:
            try:
                params = json.loads(bstack11lll11ll11_opy_)
                if bstack11l11l1_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧᘾ") in params and params.get(bstack11l11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨᘿ")) is True:
                    bstack11lll1l11l1_opy_ = bstack11l11l1_opy_ (u"ࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤᙀ")
            except Exception as bstack11lll11llll_opy_:
                logger.error(bstack11l11l1_opy_ (u"ࠨࡊࡔࡑࡑࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥ࡫ࡲࡳࡱࡵࠤ࡮ࡴࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡔࡦࡸࡡ࡮ࡵ࠽ࠤࢀࢃࠢᙁ").format(bstack11lll11llll_opy_))
        bstack11lll1l1111_opy_ = False
        from browserstack_sdk.sdk_cli.bstack1l1l11111ll_opy_ import bstack1l11ll1llll_opy_
        if test_framework_state in bstack1l11ll1llll_opy_.bstack1ll1l1lll11_opy_:
            if bstack11lll1l11l1_opy_ == bstack11llll11ll1_opy_:
                bstack11lll1l1111_opy_ = True
            bstack11lll1l11l1_opy_ = bstack11llll111ll_opy_
        try:
            platform_index = os.environ[bstack11l11l1_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡋࡑࡈࡊ࡞ࠧᙂ")]
            target_dir = os.path.join(bstack1ll1l1l1l11_opy_, bstack1ll1l11l1l1_opy_ + str(platform_index),
                                      bstack11lll1l11l1_opy_)
            if bstack11lll1l1111_opy_:
                target_dir = os.path.join(target_dir, bstack11lll1l1l11_opy_)
            os.makedirs(target_dir, exist_ok=True)
            logger.debug(bstack11l11l1_opy_ (u"ࠣࡅࡵࡩࡦࡺࡥࡥ࠱ࡹࡩࡷ࡯ࡦࡪࡧࡧࠤࡹࡧࡲࡨࡧࡷࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࠺ࠡࡽࢀࠦᙃ").format(target_dir))
            file_name = os.path.basename(bstack11lll1l1lll_opy_)
            bstack11lll1l1l1l_opy_ = os.path.join(target_dir, file_name)
            if os.path.exists(bstack11lll1l1l1l_opy_):
                base_name, extension = os.path.splitext(file_name)
                bstack11lll11lll1_opy_ = 1
                while os.path.exists(os.path.join(target_dir, base_name + str(bstack11lll11lll1_opy_) + extension)):
                    bstack11lll11lll1_opy_ += 1
                bstack11lll1l1l1l_opy_ = os.path.join(target_dir, base_name + str(bstack11lll11lll1_opy_) + extension)
            shutil.copy(bstack11lll1l1lll_opy_, bstack11lll1l1l1l_opy_)
            logger.info(bstack11l11l1_opy_ (u"ࠤࡉ࡭ࡱ࡫ࠠࡴࡷࡦࡧࡪࡹࡳࡧࡷ࡯ࡰࡾࠦࡣࡰࡲ࡬ࡩࡩࠦࡴࡰ࠼ࠣࡿࢂࠨᙄ").format(bstack11lll1l1l1l_opy_))
        except Exception as e:
            logger.error(bstack11l11l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡰࡳࡻ࡯࡮ࡨࠢࡩ࡭ࡱ࡫ࠠࡵࡱࠣࡸࡦࡸࡧࡦࡶࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࡀࠠࡼࡿࠥᙅ").format(e))
            return
        finally:
            if bstack11lll1l111l_opy_.startswith(bstack11l11l1_opy_ (u"ࠦ࡭ࡺࡴࡱ࠼࠲࠳ࠧᙆ")) or bstack11lll1l111l_opy_.startswith(bstack11l11l1_opy_ (u"ࠧ࡮ࡴࡵࡲࡶ࠾࠴࠵ࠢᙇ")):
                try:
                    if bstack11lll1l1lll_opy_ is not None and bstack11lll1l1lll_opy_.exists():
                        bstack11lll1l1lll_opy_.unlink()
                        logger.debug(bstack11l11l1_opy_ (u"ࠨࡔࡦ࡯ࡳࡳࡷࡧࡲࡺࠢࡩ࡭ࡱ࡫ࠠࡥࡧ࡯ࡩࡹ࡫ࡤ࠻ࠢࡾࢁࠧᙈ").format(bstack11lll1l1lll_opy_))
                except Exception as ex:
                    logger.error(bstack11l11l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡤࡦ࡮ࡨࡸ࡮ࡴࡧࠡࡶࡨࡱࡵࡵࡲࡢࡴࡼࠤ࡫࡯࡬ࡦ࠼ࠣࡿࢂࠨᙉ").format(ex))
    @staticmethod
    def bstack1lll1lll11_opy_() -> None:
        bstack11l11l1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡊࡥ࡭ࡧࡷࡩࡸࠦࡡ࡭࡮ࠣࡪࡴࡲࡤࡦࡴࡶࠤࡼ࡮࡯ࡴࡧࠣࡲࡦࡳࡥࡴࠢࡶࡸࡦࡸࡴࠡࡹ࡬ࡸ࡭ࠦࠢࡖࡲ࡯ࡳࡦࡪࡥࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࡸ࠳ࠢࠡࡨࡲࡰࡱࡵࡷࡦࡦࠣࡦࡾࠦࡡࠡࡰࡸࡱࡧ࡫ࡲࠡ࡫ࡱࠎࠥࠦࠠࠡࠢࠣࠤࠥࡺࡨࡦࠢࡸࡷࡪࡸࠧࡴࠢࢁ࠳࠳ࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᙊ")
        bstack11lll11l11l_opy_ = bstack1ll11ll1lll_opy_()
        pattern = re.compile(bstack11l11l1_opy_ (u"ࡴ࡙ࠥࡵࡲ࡯ࡢࡦࡨࡨࡆࡺࡴࡢࡥ࡫ࡱࡪࡴࡴࡴ࠯࡟ࡨ࠰ࠨᙋ"))
        if os.path.exists(bstack11lll11l11l_opy_):
            for item in os.listdir(bstack11lll11l11l_opy_):
                bstack11lll111ll1_opy_ = os.path.join(bstack11lll11l11l_opy_, item)
                if os.path.isdir(bstack11lll111ll1_opy_) and pattern.fullmatch(item):
                    try:
                        shutil.rmtree(bstack11lll111ll1_opy_)
                    except Exception as e:
                        logger.error(bstack11l11l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡧࡩࡱ࡫ࡴࡪࡰࡪࠤࡩ࡯ࡲࡦࡥࡷࡳࡷࡿ࠺ࠡࡽࢀࠦᙌ").format(e))
        else:
            logger.info(bstack11l11l1_opy_ (u"࡙ࠦ࡮ࡥࠡࡦ࡬ࡶࡪࡩࡴࡰࡴࡼࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠿ࠦࡻࡾࠤᙍ").format(bstack11lll11l11l_opy_))