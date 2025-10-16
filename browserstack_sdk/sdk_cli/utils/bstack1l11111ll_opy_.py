# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
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
from bstack_utils.helper import bstack1ll11l1l111_opy_
bstack11lll1lllll_opy_ = 100 * 1024 * 1024 # 100 bstack11lll11llll_opy_
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
bstack1ll111llll1_opy_ = bstack1ll11l1l111_opy_()
bstack1ll11l1ll1l_opy_ = bstack1ll11_opy_ (u"ࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨᘐ")
bstack11llll1llll_opy_ = bstack1ll11_opy_ (u"ࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥᘑ")
bstack11llll1l1ll_opy_ = bstack1ll11_opy_ (u"ࠣࡄࡸ࡭ࡱࡪࡌࡦࡸࡨࡰࠧᘒ")
bstack11llll1ll11_opy_ = bstack1ll11_opy_ (u"ࠤࡋࡳࡴࡱࡌࡦࡸࡨࡰࠧᘓ")
bstack11lll1ll111_opy_ = bstack1ll11_opy_ (u"ࠥࡆࡺ࡯࡬ࡥࡎࡨࡺࡪࡲࡈࡰࡱ࡮ࡉࡻ࡫࡮ࡵࠤᘔ")
_11lll1ll1ll_opy_ = threading.local()
def bstack1ll111lll11_opy_(test_framework_state, test_hook_state):
    bstack1ll11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡘ࡫ࡴࠡࡶ࡫ࡩࠥࡩࡵࡳࡴࡨࡲࡹࠦࡴࡦࡵࡷࠤࡪࡼࡥ࡯ࡶࠣࡷࡹࡧࡴࡦࠢ࡬ࡲࠥࡺࡨࡳࡧࡤࡨ࠲ࡲ࡯ࡤࡣ࡯ࠤࡸࡺ࡯ࡳࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࡘ࡭࡯ࡳࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡷ࡭ࡵࡵ࡭ࡦࠣࡦࡪࠦࡣࡢ࡮࡯ࡩࡩࠦࡢࡺࠢࡷ࡬ࡪࠦࡥࡷࡧࡱࡸࠥ࡮ࡡ࡯ࡦ࡯ࡩࡷࠦࠨࡴࡷࡦ࡬ࠥࡧࡳࠡࡶࡵࡥࡨࡱ࡟ࡦࡸࡨࡲࡹ࠯ࠊࠡࠢࠣࠤࡧ࡫ࡦࡰࡴࡨࠤࡦࡴࡹࠡࡨ࡬ࡰࡪࠦࡵࡱ࡮ࡲࡥࡩࡹࠠࡰࡥࡦࡹࡷ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᘕ")
    _11lll1ll1ll_opy_.test_framework_state = test_framework_state
    _11lll1ll1ll_opy_.test_hook_state = test_hook_state
def bstack11lll1l1111_opy_():
    bstack1ll11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡘࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡵࡪࡨࠤࡨࡻࡲࡳࡧࡱࡸࠥࡺࡥࡴࡶࠣࡩࡻ࡫࡮ࡵࠢࡶࡸࡦࡺࡥࠡࡨࡵࡳࡲࠦࡴࡩࡴࡨࡥࡩ࠳࡬ࡰࡥࡤࡰࠥࡹࡴࡰࡴࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷࠥࡧࠠࡵࡷࡳࡰࡪࠦࠨࡵࡧࡶࡸࡤ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࡠࡵࡷࡥࡹ࡫ࠬࠡࡶࡨࡷࡹࡥࡨࡰࡱ࡮ࡣࡸࡺࡡࡵࡧࠬࠤࡴࡸࠠࠩࡐࡲࡲࡪ࠲ࠠࡏࡱࡱࡩ࠮ࠦࡩࡧࠢࡱࡳࡹࠦࡳࡦࡶ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᘖ")
    return (
        getattr(_11lll1ll1ll_opy_, bstack1ll11_opy_ (u"࠭ࡴࡦࡵࡷࡣ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱ࡟ࡴࡶࡤࡸࡪ࠭ᘗ"), None),
        getattr(_11lll1ll1ll_opy_, bstack1ll11_opy_ (u"ࠧࡵࡧࡶࡸࡤ࡮࡯ࡰ࡭ࡢࡷࡹࡧࡴࡦࠩᘘ"), None)
    )
class bstack11ll1l11ll_opy_:
    bstack1ll11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡈ࡬ࡰࡪ࡛ࡰ࡭ࡱࡤࡨࡪࡸࠠࡱࡴࡲࡺ࡮ࡪࡥࡴࠢࡩࡹࡳࡩࡴࡪࡱࡱࡥࡱ࡯ࡴࡺࠢࡷࡳࠥࡻࡰ࡭ࡱࡤࡨࠥࡧ࡮ࠡࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥࡨࡡࡴࡧࡧࠤࡴࡴࠠࡵࡪࡨࠤ࡬࡯ࡶࡦࡰࠣࡪ࡮ࡲࡥࠡࡲࡤࡸ࡭࠴ࠊࠡࠢࠣࠤࡎࡺࠠࡴࡷࡳࡴࡴࡸࡴࡴࠢࡥࡳࡹ࡮ࠠ࡭ࡱࡦࡥࡱࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࡵࠣࡥࡳࡪࠠࡉࡖࡗࡔ࠴ࡎࡔࡕࡒࡖࠤ࡚ࡘࡌࡴ࠮ࠣࡥࡳࡪࠠࡤࡱࡳ࡭ࡪࡹࠠࡵࡪࡨࠤ࡫࡯࡬ࡦࠢ࡬ࡲࡹࡵࠠࡢࠢࡧࡩࡸ࡯ࡧ࡯ࡣࡷࡩࡩࠐࠠࠡࠢࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࠦࡷࡪࡶ࡫࡭ࡳࠦࡴࡩࡧࠣࡹࡸ࡫ࡲࠨࡵࠣ࡬ࡴࡳࡥࠡࡨࡲࡰࡩ࡫ࡲࠡࡷࡱࡨࡪࡸࠠࡿ࠱࠱ࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬࠱ࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠯ࠌࠣࠤࠥࠦࡉࡧࠢࡤࡲࠥࡵࡰࡵ࡫ࡲࡲࡦࡲࠠࡢࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠤࡵࡧࡲࡢ࡯ࡨࡸࡪࡸࠠࠩ࡫ࡱࠤࡏ࡙ࡏࡏࠢࡩࡳࡷࡳࡡࡵࠫࠣ࡭ࡸࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤࠡࡣࡱࡨࠥࡩ࡯࡯ࡶࡤ࡭ࡳࡹࠠࡢࠢࡷࡶࡺࡺࡨࡺࠢࡹࡥࡱࡻࡥࠋࠢࠣࠤࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦ࡫ࡦࡻࠣࠦࡧࡻࡩ࡭ࡦࡄࡸࡹࡧࡣࡩ࡯ࡨࡲࡹࠨࠬࠡࡶ࡫ࡩࠥ࡬ࡩ࡭ࡧࠣࡻ࡮ࡲ࡬ࠡࡤࡨࠤࡵࡲࡡࡤࡧࡧࠤ࡮ࡴࠠࡵࡪࡨࠤࠧࡈࡵࡪ࡮ࡧࡐࡪࡼࡥ࡭ࠤࠣࡪࡴࡲࡤࡦࡴ࠾ࠤࡴࡺࡨࡦࡴࡺ࡭ࡸ࡫ࠬࠋࠢࠣࠤࠥ࡯ࡴࠡࡦࡨࡪࡦࡻ࡬ࡵࡵࠣࡸࡴࠦࠢࡕࡧࡶࡸࡑ࡫ࡶࡦ࡮ࠥ࠲ࠏࠦࠠࠡࠢࡗ࡬࡮ࡹࠠࡷࡧࡵࡷ࡮ࡵ࡮ࠡࡱࡩࠤࡦࡪࡤࡠࡣࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠥ࡯ࡳࠡࡣࠣࡺࡴ࡯ࡤࠡ࡯ࡨࡸ࡭ࡵࡤ⠕࡫ࡷࠤ࡭ࡧ࡮ࡥ࡮ࡨࡷࠥࡧ࡬࡭ࠢࡨࡶࡷࡵࡲࡴࠢࡪࡶࡦࡩࡥࡧࡷ࡯ࡰࡾࠦࡢࡺࠢ࡯ࡳ࡬࡭ࡩ࡯ࡩࠍࠤࠥࠦࠠࡵࡪࡨࡱࠥࡧ࡮ࡥࠢࡶ࡭ࡲࡶ࡬ࡺࠢࡵࡩࡹࡻࡲ࡯࡫ࡱ࡫ࠥࡽࡩࡵࡪࡲࡹࡹࠦࡴࡩࡴࡲࡻ࡮ࡴࡧࠡࡧࡻࡧࡪࡶࡴࡪࡱࡱࡷ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᘙ")
    @staticmethod
    def upload_attachment(bstack11lll1ll11l_opy_: str, *bstack11lll1l1lll_opy_) -> None:
        if not bstack11lll1ll11l_opy_ or not bstack11lll1ll11l_opy_.strip():
            logger.error(bstack1ll11_opy_ (u"ࠤࡤࡨࡩࡥࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࠣࡪࡦ࡯࡬ࡦࡦ࠽ࠤࡕࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡦࡪ࡮ࡨࠤࡵࡧࡴࡩࠢ࡬ࡷࠥ࡫࡭ࡱࡶࡼࠤࡴࡸࠠࡏࡱࡱࡩ࠳ࠨᘚ"))
            return
        bstack11lll1lll1l_opy_ = bstack11lll1l1lll_opy_[0] if bstack11lll1l1lll_opy_ and len(bstack11lll1l1lll_opy_) > 0 else None
        bstack11lll1l11l1_opy_ = None
        test_framework_state, test_hook_state = bstack11lll1l1111_opy_()
        try:
            if bstack11lll1ll11l_opy_.startswith(bstack1ll11_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᘛ")) or bstack11lll1ll11l_opy_.startswith(bstack1ll11_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᘜ")):
                logger.debug(bstack1ll11_opy_ (u"ࠧࡖࡡࡵࡪࠣ࡭ࡸࠦࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡦࠣࡥࡸࠦࡕࡓࡎ࠾ࠤࡩࡵࡷ࡯࡮ࡲࡥࡩ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡦࡪ࡮ࡨ࠲ࠧᘝ"))
                url = bstack11lll1ll11l_opy_
                bstack11lll1l1l11_opy_ = str(uuid.uuid4())
                bstack11llll11111_opy_ = os.path.basename(urllib.request.urlparse(url).path)
                if not bstack11llll11111_opy_ or not bstack11llll11111_opy_.strip():
                    bstack11llll11111_opy_ = bstack11lll1l1l11_opy_
                temp_file = tempfile.NamedTemporaryFile(delete=False,
                                                        prefix=bstack1ll11_opy_ (u"ࠨࡵࡱ࡮ࡲࡥࡩࡥࠢᘞ") + bstack11lll1l1l11_opy_ + bstack1ll11_opy_ (u"ࠢࡠࠤᘟ"),
                                                        suffix=bstack1ll11_opy_ (u"ࠣࡡࠥᘠ") + bstack11llll11111_opy_)
                with urllib.request.urlopen(url) as response, open(temp_file.name, bstack1ll11_opy_ (u"ࠩࡺࡦࠬᘡ")) as out_file:
                    shutil.copyfileobj(response, out_file)
                bstack11lll1l11l1_opy_ = Path(temp_file.name)
                logger.debug(bstack1ll11_opy_ (u"ࠥࡈࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࠠࡧ࡫࡯ࡩࠥࡺ࡯ࠡࡶࡨࡱࡵࡵࡲࡢࡴࡼࠤࡱࡵࡣࡢࡶ࡬ࡳࡳࡀࠠࡼࡿࠥᘢ").format(bstack11lll1l11l1_opy_))
            else:
                bstack11lll1l11l1_opy_ = Path(bstack11lll1ll11l_opy_)
                logger.debug(bstack1ll11_opy_ (u"ࠦࡕࡧࡴࡩࠢ࡬ࡷࠥ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡥࠢࡤࡷࠥࡲ࡯ࡤࡣ࡯ࠤ࡫࡯࡬ࡦ࠼ࠣࡿࢂࠨᘣ").format(bstack11lll1l11l1_opy_))
        except Exception as e:
            logger.error(bstack1ll11_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡱࡥࡸࡦ࡯࡮ࠡࡨ࡬ࡰࡪࠦࡦࡳࡱࡰࠤࡵࡧࡴࡩ࠱ࡘࡖࡑࡀࠠࡼࡿࠥᘤ").format(e))
            return
        if bstack11lll1l11l1_opy_ is None or not bstack11lll1l11l1_opy_.exists():
            logger.error(bstack1ll11_opy_ (u"ࠨࡓࡰࡷࡵࡧࡪࠦࡦࡪ࡮ࡨࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠿ࠦࡻࡾࠤᘥ").format(bstack11lll1l11l1_opy_))
            return
        if bstack11lll1l11l1_opy_.stat().st_size > bstack11lll1lllll_opy_:
            logger.error(bstack1ll11_opy_ (u"ࠢࡇ࡫࡯ࡩࠥࡹࡩࡻࡧࠣࡩࡽࡩࡥࡦࡦࡶࠤࡲࡧࡸࡪ࡯ࡸࡱࠥࡧ࡬࡭ࡱࡺࡩࡩࠦࡳࡪࡼࡨࠤࡴ࡬ࠠࡼࡿࠥᘦ").format(bstack11lll1lllll_opy_))
            return
        bstack11lll1l11ll_opy_ = bstack1ll11_opy_ (u"ࠣࡖࡨࡷࡹࡒࡥࡷࡧ࡯ࠦᘧ")
        if bstack11lll1lll1l_opy_:
            try:
                params = json.loads(bstack11lll1lll1l_opy_)
                if bstack1ll11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࠦᘨ") in params and params.get(bstack1ll11_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡃࡷࡸࡦࡩࡨ࡮ࡧࡱࡸࠧᘩ")) is True:
                    bstack11lll1l11ll_opy_ = bstack1ll11_opy_ (u"ࠦࡇࡻࡩ࡭ࡦࡏࡩࡻ࡫࡬ࠣᘪ")
            except Exception as bstack11lll1l1ll1_opy_:
                logger.error(bstack1ll11_opy_ (u"ࠧࡐࡓࡐࡐࠣࡴࡦࡸࡳࡪࡰࡪࠤࡪࡸࡲࡰࡴࠣ࡭ࡳࠦࡡࡵࡶࡤࡧ࡭ࡳࡥ࡯ࡶࡓࡥࡷࡧ࡭ࡴ࠼ࠣࡿࢂࠨᘫ").format(bstack11lll1l1ll1_opy_))
        bstack11lll1llll1_opy_ = False
        from browserstack_sdk.sdk_cli.bstack1l1l1llllll_opy_ import bstack1l1l11lll1l_opy_
        if test_framework_state in bstack1l1l11lll1l_opy_.bstack1ll11llll11_opy_:
            if bstack11lll1l11ll_opy_ == bstack11llll1l1ll_opy_:
                bstack11lll1llll1_opy_ = True
            bstack11lll1l11ll_opy_ = bstack11llll1ll11_opy_
        try:
            platform_index = os.environ[bstack1ll11_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡊࡐࡇࡉ࡝࠭ᘬ")]
            target_dir = os.path.join(bstack1ll111llll1_opy_, bstack1ll11l1ll1l_opy_ + str(platform_index),
                                      bstack11lll1l11ll_opy_)
            if bstack11lll1llll1_opy_:
                target_dir = os.path.join(target_dir, bstack11lll1ll111_opy_)
            os.makedirs(target_dir, exist_ok=True)
            logger.debug(bstack1ll11_opy_ (u"ࠢࡄࡴࡨࡥࡹ࡫ࡤ࠰ࡸࡨࡶ࡮࡬ࡩࡦࡦࠣࡸࡦࡸࡧࡦࡶࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࡀࠠࡼࡿࠥᘭ").format(target_dir))
            file_name = os.path.basename(bstack11lll1l11l1_opy_)
            bstack11lll1l111l_opy_ = os.path.join(target_dir, file_name)
            if os.path.exists(bstack11lll1l111l_opy_):
                base_name, extension = os.path.splitext(file_name)
                bstack11lll1ll1l1_opy_ = 1
                while os.path.exists(os.path.join(target_dir, base_name + str(bstack11lll1ll1l1_opy_) + extension)):
                    bstack11lll1ll1l1_opy_ += 1
                bstack11lll1l111l_opy_ = os.path.join(target_dir, base_name + str(bstack11lll1ll1l1_opy_) + extension)
            shutil.copy(bstack11lll1l11l1_opy_, bstack11lll1l111l_opy_)
            logger.info(bstack1ll11_opy_ (u"ࠣࡈ࡬ࡰࡪࠦࡳࡶࡥࡦࡩࡸࡹࡦࡶ࡮࡯ࡽࠥࡩ࡯ࡱ࡫ࡨࡨࠥࡺ࡯࠻ࠢࡾࢁࠧᘮ").format(bstack11lll1l111l_opy_))
        except Exception as e:
            logger.error(bstack1ll11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡ࡯ࡲࡺ࡮ࡴࡧࠡࡨ࡬ࡰࡪࠦࡴࡰࠢࡷࡥࡷ࡭ࡥࡵࠢࡧ࡭ࡷ࡫ࡣࡵࡱࡵࡽ࠿ࠦࡻࡾࠤᘯ").format(e))
            return
        finally:
            if bstack11lll1ll11l_opy_.startswith(bstack1ll11_opy_ (u"ࠥ࡬ࡹࡺࡰ࠻࠱࠲ࠦᘰ")) or bstack11lll1ll11l_opy_.startswith(bstack1ll11_opy_ (u"ࠦ࡭ࡺࡴࡱࡵ࠽࠳࠴ࠨᘱ")):
                try:
                    if bstack11lll1l11l1_opy_ is not None and bstack11lll1l11l1_opy_.exists():
                        bstack11lll1l11l1_opy_.unlink()
                        logger.debug(bstack1ll11_opy_ (u"࡚ࠧࡥ࡮ࡲࡲࡶࡦࡸࡹࠡࡨ࡬ࡰࡪࠦࡤࡦ࡮ࡨࡸࡪࡪ࠺ࠡࡽࢀࠦᘲ").format(bstack11lll1l11l1_opy_))
                except Exception as ex:
                    logger.error(bstack1ll11_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡪࡥ࡭ࡧࡷ࡭ࡳ࡭ࠠࡵࡧࡰࡴࡴࡸࡡࡳࡻࠣࡪ࡮ࡲࡥ࠻ࠢࡾࢁࠧᘳ").format(ex))
    @staticmethod
    def bstack111l111ll_opy_() -> None:
        bstack1ll11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡉ࡫࡬ࡦࡶࡨࡷࠥࡧ࡬࡭ࠢࡩࡳࡱࡪࡥࡳࡵࠣࡻ࡭ࡵࡳࡦࠢࡱࡥࡲ࡫ࡳࠡࡵࡷࡥࡷࡺࠠࡸ࡫ࡷ࡬ࠥࠨࡕࡱ࡮ࡲࡥࡩ࡫ࡤࡂࡶࡷࡥࡨ࡮࡭ࡦࡰࡷࡷ࠲ࠨࠠࡧࡱ࡯ࡰࡴࡽࡥࡥࠢࡥࡽࠥࡧࠠ࡯ࡷࡰࡦࡪࡸࠠࡪࡰࠍࠤࠥࠦࠠࠡࠢࠣࠤࡹ࡮ࡥࠡࡷࡶࡩࡷ࠭ࡳࠡࢀ࠲࠲ࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᘴ")
        bstack11lll1l1l1l_opy_ = bstack1ll11l1l111_opy_()
        pattern = re.compile(bstack1ll11_opy_ (u"ࡳࠤࡘࡴࡱࡵࡡࡥࡧࡧࡅࡹࡺࡡࡤࡪࡰࡩࡳࡺࡳ࠮࡞ࡧ࠯ࠧᘵ"))
        if os.path.exists(bstack11lll1l1l1l_opy_):
            for item in os.listdir(bstack11lll1l1l1l_opy_):
                bstack11lll1lll11_opy_ = os.path.join(bstack11lll1l1l1l_opy_, item)
                if os.path.isdir(bstack11lll1lll11_opy_) and pattern.fullmatch(item):
                    try:
                        shutil.rmtree(bstack11lll1lll11_opy_)
                    except Exception as e:
                        logger.error(bstack1ll11_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡦࡨࡰࡪࡺࡩ࡯ࡩࠣࡨ࡮ࡸࡥࡤࡶࡲࡶࡾࡀࠠࡼࡿࠥᘶ").format(e))
        else:
            logger.info(bstack1ll11_opy_ (u"ࠥࡘ࡭࡫ࠠࡥ࡫ࡵࡩࡨࡺ࡯ࡳࡻࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠾ࠥࢁࡽࠣᘷ").format(bstack11lll1l1l1l_opy_))