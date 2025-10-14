# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
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
from bstack_utils.helper import bstack1ll1l11ll11_opy_
bstack11lll1lll11_opy_ = 100 * 1024 * 1024 # 100 bstack11lll1l1ll1_opy_
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
bstack1ll1l1l1ll1_opy_ = bstack1ll1l11ll11_opy_()
bstack1ll11ll1111_opy_ = bstack11l1l11_opy_ (u"ࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨᘉ")
bstack11llll1l1ll_opy_ = bstack11l1l11_opy_ (u"ࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥᘊ")
bstack11llll1l1l1_opy_ = bstack11l1l11_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧᘋ")
bstack11llll1l11l_opy_ = bstack11l1l11_opy_ (u"ࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰࠧᘌ")
bstack11lll1l1l11_opy_ = bstack11l1l11_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠤᘍ")
_11lll1llll1_opy_ = threading.local()
def bstack1ll11l11111_opy_(test_framework_state, test_hook_state):
    bstack11l1l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡘ࡫ࡴࠡࡶ࡫ࡩࠥࡩࡵࡳࡴࡨࡲࡹࠦࡴࡦࡵࡷࠤࡪࡼࡥ࡯ࡶࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡺࡨࡳࡧࡤࡨ࠲ࡲ࡯ࡤࡣ࡯ࠤࡸࡺ࡯ࡳࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࡘ࡭࡯ࡳࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡷ࡭ࡵࡵ࡭ࡦࠣࡦࡪࠦࡣࡢ࡮࡯ࡩࡩࠦࡢࡺࠢࡷ࡬ࡪࠦࡥࡷࡧࡱࡸࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࠦࠨࡴࡷࡦ࡬ࠥࡧࡳࠡࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹ࠯ࠊࠡࠢࠣࠤࡧ࡫ࡦࡰࡴࡨࠤࡦࡴࡹࠡࡨ࡬ࡰࡪࠦࡵࡱ࡮ࡲࡥࡩࡹࠠࡰࡥࡦࡹࡷ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᘎ")
    _11lll1llll1_opy_.test_framework_state = test_framework_state
    _11lll1llll1_opy_.test_hook_state = test_hook_state
def bstack11lll1l11l1_opy_():
    bstack11l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡘࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡵࡪࡨࠤࡨࡻࡲࡳࡧࡱࡸࠥࡺࡥࡴࡶࠣࡩࡻ࡫࡮ࡵࠢࡶࡸࡦࡺࡥࠡࡨࡵࡳࡲࠦࡴࡩࡴࡨࡥࡩ࠳࡬ࡰࡥࡤࡰࠥࡹࡴࡰࡴࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷࠥࡧࠠࡵࡷࡳࡰࡪࠦࠨࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࠬࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࠬࠤࡴࡸࠠࠩࡐࡲࡲࡪ࠲ࠠࡏࡱࡱࡩ࠮ࠦࡩࡧࠢࡱࡳࡹࠦࡳࡦࡶ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᘏ")
    return (
        getattr(_11lll1llll1_opy_, bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪ࠭ᘐ"), None),
        getattr(_11lll1llll1_opy_, bstack11l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࠩᘑ"), None)
    )
class bstack1111l1l111_opy_:
    bstack11l1l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡈ࡬ࡰࡪ࡛ࡰ࡭ࡱࡤࡨࡪࡸࠠࡱࡴࡲࡺ࡮ࡪࡥࡴࠢࡩࡹࡳࡩࡴࡪࡱࡱࡥࡱ࡯ࡴࡺࠢࡷࡳࠥࡻࡰ࡭ࡱࡤࡨࠥࡧ࡮ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࡨࡡࡴࡧࡧࠤࡴࡴࠠࡵࡪࡨࠤ࡬࡯ࡶࡦࡰࠣࡪ࡮ࡲࡥࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤࡎࡺࠠࡴࡷࡳࡴࡴࡸࡴࡴࠢࡥࡳࡹ࡮ࠠ࡭ࡱࡦࡥࡱࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࡵࠣࡥࡳࡪࠠࡉࡖࡗࡔ࠴ࡎࡔࡕࡒࡖࠤ࡚ࡘࡌࡴ࠮ࠣࡥࡳࡪࠠࡤࡱࡳ࡭ࡪࡹࠠࡵࡪࡨࠤ࡫࡯࡬ࡦࠢ࡬ࡲࡹࡵࠠࡢࠢࡧࡩࡸ࡯ࡧ࡯ࡣࡷࡩࡩࠐࠠࠡࠢࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡷࡪࡶ࡫࡭ࡳࠦࡴࡩࡧࠣࡹࡸ࡫ࡲࠨࡵࠣ࡬ࡴࡳࡥࠡࡨࡲࡰࡩ࡫ࡲࠡࡷࡱࡨࡪࡸࠠࡿ࠱࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠱ࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠯ࠌࠣࠤࠥࠦࡉࡧࠢࡤࡲࠥࡵࡰࡵ࡫ࡲࡲࡦࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠤࡵࡧࡲࡢ࡯ࡨࡸࡪࡸࠠࠩ࡫ࡱࠤࡏ࡙ࡏࡏࠢࡩࡳࡷࡳࡡࡵࠫࠣ࡭ࡸࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤࠡࡣࡱࡨࠥࡩ࡯࡯ࡶࡤ࡭ࡳࡹࠠࡢࠢࡷࡶࡺࡺࡨࡺࠢࡹࡥࡱࡻࡥࠋࠢࠣࠤࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦ࡫ࡦࡻࠣࠦࡧࡻࡩ࡭ࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨࠬࠡࡶ࡫ࡩࠥ࡬ࡩ࡭ࡧࠣࡻ࡮ࡲ࡬ࠡࡤࡨࠤࡵࡲࡡࡤࡧࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤࠣࡪࡴࡲࡤࡦࡴ࠾ࠤࡴࡺࡨࡦࡴࡺ࡭ࡸ࡫ࠬࠋࠢࠣࠤࠥ࡯ࡴࠡࡦࡨࡪࡦࡻ࡬ࡵࡵࠣࡸࡴࠦࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥ࠲ࠏࠦࠠࠡࠢࡗ࡬࡮ࡹࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡱࡩࠤࡦࡪࡤࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥ࡯ࡳࠡࡣࠣࡺࡴ࡯ࡤࠡ࡯ࡨࡸ࡭ࡵࡤ⠕࡫ࡷࠤ࡭ࡧ࡮ࡥ࡮ࡨࡷࠥࡧ࡬࡭ࠢࡨࡶࡷࡵࡲࡴࠢࡪࡶࡦࡩࡥࡧࡷ࡯ࡰࡾࠦࡢࡺࠢ࡯ࡳ࡬࡭ࡩ࡯ࡩࠍࠤࠥࠦࠠࡵࡪࡨࡱࠥࡧ࡮ࡥࠢࡶ࡭ࡲࡶ࡬ࡺࠢࡵࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥࡽࡩࡵࡪࡲࡹࡹࠦࡴࡩࡴࡲࡻ࡮ࡴࡧࠡࡧࡻࡧࡪࡶࡴࡪࡱࡱࡷ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᘒ")
    @staticmethod
    def upload_attachment(bstack11lll11ll1l_opy_: str, *bstack11lll1l1111_opy_) -> None:
        if not bstack11lll11ll1l_opy_ or not bstack11lll11ll1l_opy_.strip():
            logger.error(bstack11l1l11_opy_ (u"ࠤࡤࡨࡩࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡕࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࠢ࡬ࡷࠥ࡫࡭ࡱࡶࡼࠤࡴࡸࠠࡏࡱࡱࡩ࠳ࠨᘓ"))
            return
        bstack11lll1lll1l_opy_ = bstack11lll1l1111_opy_[0] if bstack11lll1l1111_opy_ and len(bstack11lll1l1111_opy_) > 0 else None
        bstack11lll11llll_opy_ = None
        test_framework_state, test_hook_state = bstack11lll1l11l1_opy_()
        try:
            if bstack11lll11ll1l_opy_.startswith(bstack11l1l11_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᘔ")) or bstack11lll11ll1l_opy_.startswith(bstack11l1l11_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᘕ")):
                logger.debug(bstack11l1l11_opy_ (u"ࠧࡖࡡࡵࡪࠣ࡭ࡸࠦࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡦࠣࡥࡸࠦࡕࡓࡎ࠾ࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡦࡪ࡮ࡨ࠲ࠧᘖ"))
                url = bstack11lll11ll1l_opy_
                bstack11lll1ll11l_opy_ = str(uuid.uuid4())
                bstack11lll1l1l1l_opy_ = os.path.basename(urllib.request.urlparse(url).path)
                if not bstack11lll1l1l1l_opy_ or not bstack11lll1l1l1l_opy_.strip():
                    bstack11lll1l1l1l_opy_ = bstack11lll1ll11l_opy_
                temp_file = tempfile.NamedTemporaryFile(delete=False,
                                                        prefix=bstack11l1l11_opy_ (u"ࠨࡵࡱ࡮ࡲࡥࡩࡥࠢᘗ") + bstack11lll1ll11l_opy_ + bstack11l1l11_opy_ (u"ࠢࡠࠤᘘ"),
                                                        suffix=bstack11l1l11_opy_ (u"ࠣࡡࠥᘙ") + bstack11lll1l1l1l_opy_)
                with urllib.request.urlopen(url) as response, open(temp_file.name, bstack11l1l11_opy_ (u"ࠩࡺࡦࠬᘚ")) as out_file:
                    shutil.copyfileobj(response, out_file)
                bstack11lll11llll_opy_ = Path(temp_file.name)
                logger.debug(bstack11l1l11_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡧ࡫࡯ࡩࠥࡺ࡯ࠡࡶࡨࡱࡵࡵࡲࡢࡴࡼࠤࡱࡵࡣࡢࡶ࡬ࡳࡳࡀࠠࡼࡿࠥᘛ").format(bstack11lll11llll_opy_))
            else:
                bstack11lll11llll_opy_ = Path(bstack11lll11ll1l_opy_)
                logger.debug(bstack11l1l11_opy_ (u"ࠦࡕࡧࡴࡩࠢ࡬ࡷࠥ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡥࠢࡤࡷࠥࡲ࡯ࡤࡣ࡯ࠤ࡫࡯࡬ࡦ࠼ࠣࡿࢂࠨᘜ").format(bstack11lll11llll_opy_))
        except Exception as e:
            logger.error(bstack11l1l11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡱࡥࡸࡦ࡯࡮ࠡࡨ࡬ࡰࡪࠦࡦࡳࡱࡰࠤࡵࡧࡴࡩ࠱ࡘࡖࡑࡀࠠࡼࡿࠥᘝ").format(e))
            return
        if bstack11lll11llll_opy_ is None or not bstack11lll11llll_opy_.exists():
            logger.error(bstack11l1l11_opy_ (u"ࠨࡓࡰࡷࡵࡧࡪࠦࡦࡪ࡮ࡨࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠿ࠦࡻࡾࠤᘞ").format(bstack11lll11llll_opy_))
            return
        if bstack11lll11llll_opy_.stat().st_size > bstack11lll1lll11_opy_:
            logger.error(bstack11l1l11_opy_ (u"ࠢࡇ࡫࡯ࡩࠥࡹࡩࡻࡧࠣࡩࡽࡩࡥࡦࡦࡶࠤࡲࡧࡸࡪ࡯ࡸࡱࠥࡧ࡬࡭ࡱࡺࡩࡩࠦࡳࡪࡼࡨࠤࡴ࡬ࠠࡼࡿࠥᘟ").format(bstack11lll1lll11_opy_))
            return
        bstack11lll1ll1ll_opy_ = bstack11l1l11_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦᘠ")
        if bstack11lll1lll1l_opy_:
            try:
                params = json.loads(bstack11lll1lll1l_opy_)
                if bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠦᘡ") in params and params.get(bstack11l1l11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧᘢ")) is True:
                    bstack11lll1ll1ll_opy_ = bstack11l1l11_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣᘣ")
            except Exception as bstack11lll1l1lll_opy_:
                logger.error(bstack11l1l11_opy_ (u"ࠧࡐࡓࡐࡐࠣࡴࡦࡸࡳࡪࡰࡪࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡓࡥࡷࡧ࡭ࡴ࠼ࠣࡿࢂࠨᘤ").format(bstack11lll1l1lll_opy_))
        bstack11lll1l111l_opy_ = False
        from browserstack_sdk.sdk_cli.bstack1l1l1l1llll_opy_ import bstack1l11lll11l1_opy_
        if test_framework_state in bstack1l11lll11l1_opy_.bstack1ll11111ll1_opy_:
            if bstack11lll1ll1ll_opy_ == bstack11llll1l1l1_opy_:
                bstack11lll1l111l_opy_ = True
            bstack11lll1ll1ll_opy_ = bstack11llll1l11l_opy_
        try:
            platform_index = os.environ[bstack11l1l11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᘥ")]
            target_dir = os.path.join(bstack1ll1l1l1ll1_opy_, bstack1ll11ll1111_opy_ + str(platform_index),
                                      bstack11lll1ll1ll_opy_)
            if bstack11lll1l111l_opy_:
                target_dir = os.path.join(target_dir, bstack11lll1l1l11_opy_)
            os.makedirs(target_dir, exist_ok=True)
            logger.debug(bstack11l1l11_opy_ (u"ࠢࡄࡴࡨࡥࡹ࡫ࡤ࠰ࡸࡨࡶ࡮࡬ࡩࡦࡦࠣࡸࡦࡸࡧࡦࡶࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࡀࠠࡼࡿࠥᘦ").format(target_dir))
            file_name = os.path.basename(bstack11lll11llll_opy_)
            bstack11lll1ll111_opy_ = os.path.join(target_dir, file_name)
            if os.path.exists(bstack11lll1ll111_opy_):
                base_name, extension = os.path.splitext(file_name)
                bstack11lll1l11ll_opy_ = 1
                while os.path.exists(os.path.join(target_dir, base_name + str(bstack11lll1l11ll_opy_) + extension)):
                    bstack11lll1l11ll_opy_ += 1
                bstack11lll1ll111_opy_ = os.path.join(target_dir, base_name + str(bstack11lll1l11ll_opy_) + extension)
            shutil.copy(bstack11lll11llll_opy_, bstack11lll1ll111_opy_)
            logger.info(bstack11l1l11_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥࡩ࡯ࡱ࡫ࡨࡨࠥࡺ࡯࠻ࠢࡾࢁࠧᘧ").format(bstack11lll1ll111_opy_))
        except Exception as e:
            logger.error(bstack11l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡯ࡲࡺ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦࡴࡰࠢࡷࡥࡷ࡭ࡥࡵࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠿ࠦࡻࡾࠤᘨ").format(e))
            return
        finally:
            if bstack11lll11ll1l_opy_.startswith(bstack11l1l11_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᘩ")) or bstack11lll11ll1l_opy_.startswith(bstack11l1l11_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᘪ")):
                try:
                    if bstack11lll11llll_opy_ is not None and bstack11lll11llll_opy_.exists():
                        bstack11lll11llll_opy_.unlink()
                        logger.debug(bstack11l1l11_opy_ (u"࡚ࠧࡥ࡮ࡲࡲࡶࡦࡸࡹࠡࡨ࡬ࡰࡪࠦࡤࡦ࡮ࡨࡸࡪࡪ࠺ࠡࡽࢀࠦᘫ").format(bstack11lll11llll_opy_))
                except Exception as ex:
                    logger.error(bstack11l1l11_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡵࡧࡰࡴࡴࡸࡡࡳࡻࠣࡪ࡮ࡲࡥ࠻ࠢࡾࢁࠧᘬ").format(ex))
    @staticmethod
    def bstack1l11ll1111_opy_() -> None:
        bstack11l1l11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡉ࡫࡬ࡦࡶࡨࡷࠥࡧ࡬࡭ࠢࡩࡳࡱࡪࡥࡳࡵࠣࡻ࡭ࡵࡳࡦࠢࡱࡥࡲ࡫ࡳࠡࡵࡷࡥࡷࡺࠠࡸ࡫ࡷ࡬ࠥࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨࠠࡧࡱ࡯ࡰࡴࡽࡥࡥࠢࡥࡽࠥࡧࠠ࡯ࡷࡰࡦࡪࡸࠠࡪࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤࡹ࡮ࡥࠡࡷࡶࡩࡷ࠭ࡳࠡࢀ࠲࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᘭ")
        bstack11lll11lll1_opy_ = bstack1ll1l11ll11_opy_()
        pattern = re.compile(bstack11l1l11_opy_ (u"ࡳࠤࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠮࡞ࡧ࠯ࠧᘮ"))
        if os.path.exists(bstack11lll11lll1_opy_):
            for item in os.listdir(bstack11lll11lll1_opy_):
                bstack11lll1ll1l1_opy_ = os.path.join(bstack11lll11lll1_opy_, item)
                if os.path.isdir(bstack11lll1ll1l1_opy_) and pattern.fullmatch(item):
                    try:
                        shutil.rmtree(bstack11lll1ll1l1_opy_)
                    except Exception as e:
                        logger.error(bstack11l1l11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࡀࠠࡼࡿࠥᘯ").format(e))
        else:
            logger.info(bstack11l1l11_opy_ (u"ࠥࡘ࡭࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠾ࠥࢁࡽࠣᘰ").format(bstack11lll11lll1_opy_))