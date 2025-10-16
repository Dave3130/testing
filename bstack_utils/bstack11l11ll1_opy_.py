# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1ll1ll1_opy_ import bstack11lll111l11_opy_
from bstack_utils.bstack1111l1l1_opy_ import bstack11l111ll_opy_
from bstack_utils.helper import bstack11l11l111l_opy_
import json
class bstack11l11lll_opy_:
    _1ll1ll11lll_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack1111l11ll1l_opy_ = bstack11lll111l11_opy_(self.config, logger)
        self.bstack1111l1l1_opy_ = bstack11l111ll_opy_.bstack11111l1l_opy_(config=self.config)
        self.bstack1111l111l1l_opy_ = {}
        self.bstack111l11l1_opy_ = False
        self.bstack1111l111lll_opy_ = (
            self.__1111l111ll1_opy_()
            and self.bstack1111l1l1_opy_ is not None
            and self.bstack1111l1l1_opy_.bstack111ll111_opy_()
            and config.get(bstack1lllll1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪẉ"), None) is not None
            and config.get(bstack1lllll1_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩẊ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack11111l1l_opy_(cls, config, logger):
        if cls._1ll1ll11lll_opy_ is None and config is not None:
            cls._1ll1ll11lll_opy_ = bstack11l11lll_opy_(config, logger)
        return cls._1ll1ll11lll_opy_
    def bstack111ll111_opy_(self):
        bstack1lllll1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡉࡵࠠ࡯ࡱࡷࠤࡦࡶࡰ࡭ࡻࠣࡸࡪࡹࡴࠡࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡻ࡭࡫࡮࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࠳ࠠࡐ࠳࠴ࡽࠥ࡯ࡳࠡࡰࡲࡸࠥ࡫࡮ࡢࡤ࡯ࡩࡩࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࠰ࠤࡔࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡩࡴࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠣ࡭ࡸࠦࡎࡰࡰࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࠮ࠢࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠥ࡯ࡳࠡࡐࡲࡲࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥẋ")
        return self.bstack1111l111lll_opy_ and self.bstack1111l11ll11_opy_()
    def bstack1111l11ll11_opy_(self):
        bstack1111l111l11_opy_ = os.getenv(bstack1lllll1_opy_ (u"ࠨࡈࡕࡅࡒࡋࡗࡐࡔࡎࡣ࡚࡙ࡅࡅࠩẌ"), self.config.get(bstack1lllll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬẍ"), None))
        return bstack1111l111l11_opy_ in bstack11l1l1ll1ll_opy_
    def __1111l111ll1_opy_(self):
        bstack11ll1l11ll1_opy_ = False
        for fw in bstack11l1l1111ll_opy_:
            if fw in self.config.get(bstack1lllll1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭Ẏ"), bstack1lllll1_opy_ (u"ࠫࠬẏ")):
                bstack11ll1l11ll1_opy_ = True
        return bstack11l11l111l_opy_(self.config.get(bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶࡒࡦࡸ࡫ࡲࡷࡣࡥ࡭ࡱ࡯ࡴࡺࠩẐ"), bstack11ll1l11ll1_opy_))
    def bstack1111l11l11l_opy_(self):
        return (not self.bstack111ll111_opy_() and
                self.bstack1111l1l1_opy_ is not None and self.bstack1111l1l1_opy_.bstack111ll111_opy_())
    def bstack1111l11l1l1_opy_(self):
        if not self.bstack1111l11l11l_opy_():
            return
        if self.config.get(bstack1lllll1_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫẑ"), None) is None or self.config.get(bstack1lllll1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪẒ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack1lllll1_opy_ (u"ࠣࡖࡨࡷࡹࠦࡒࡦࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡧࡦࡴࠧࡵࠢࡺࡳࡷࡱࠠࡢࡵࠣࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠦ࡯ࡳࠢࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠠࡪࡵࠣࡲࡺࡲ࡬࠯ࠢࡓࡰࡪࡧࡳࡦࠢࡶࡩࡹࠦࡡࠡࡰࡲࡲ࠲ࡴࡵ࡭࡮ࠣࡺࡦࡲࡵࡦ࠰ࠥẓ"))
        if not self.__1111l111ll1_opy_():
            self.logger.info(bstack1lllll1_opy_ (u"ࠤࡗࡩࡸࡺࠠࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡨࡧ࡮ࠨࡶࠣࡻࡴࡸ࡫ࠡࡣࡶࠤࡹ࡫ࡳࡵࡔࡨࡴࡴࡸࡴࡪࡰࡪࠤ࡮ࡹࠠࡥ࡫ࡶࡥࡧࡲࡥࡥ࠰ࠣࡔࡱ࡫ࡡࡴࡧࠣࡩࡳࡧࡢ࡭ࡧࠣ࡭ࡹࠦࡦࡳࡱࡰࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭࠱ࡽࡲࡲࠠࡧ࡫࡯ࡩ࠳ࠨẔ"))
    def bstack1111l11l111_opy_(self):
        return self.bstack111l11l1_opy_
    def bstack1111ll11_opy_(self, bstack1111l11l1ll_opy_):
        self.bstack111l11l1_opy_ = bstack1111l11l1ll_opy_
        self.bstack11l1l11l_opy_(bstack1lllll1_opy_ (u"ࠥࡥࡵࡶ࡬ࡪࡧࡧࠦẕ"), bstack1111l11l1ll_opy_)
    def bstack1llllll11_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡠࡸࡥࡰࡴࡧࡩࡷࡥࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࡠࠤࡓࡵࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡦࡰࡴࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫࠳ࠨẖ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack1111l1l1_opy_.bstack11l111l111l_opy_()
            if self.bstack1111l1l1_opy_ is not None:
                orchestration_strategy = self.bstack1111l1l1_opy_.bstack1ll1l1llll_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack1lllll1_opy_ (u"ࠧࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡴࡳࡣࡷࡩ࡬ࡿࠠࡪࡵࠣࡒࡴࡴࡥ࠯ࠢࡆࡥࡳࡴ࡯ࡵࠢࡳࡶࡴࡩࡥࡦࡦࠣࡻ࡮ࡺࡨࠡࡶࡨࡷࡹࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡦࡵࡶ࡭ࡴࡴ࠮ࠣẗ"))
                return None
            self.logger.info(bstack1lllll1_opy_ (u"ࠨࡒࡦࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡸ࡫ࡷ࡬ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡹࡴࡳࡣࡷࡩ࡬ࡿ࠺ࠡࡽࢀࠦẘ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack1lllll1_opy_ (u"ࠢࡖࡵ࡬ࡲ࡬ࠦࡃࡍࡋࠣࡪࡱࡵࡷࠡࡨࡲࡶࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠰ࠥẙ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠣࡗࡶ࡭ࡳ࡭ࠠࡴࡦ࡮ࠤ࡫ࡲ࡯ࡸࠢࡩࡳࡷࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦẚ"))
                self.bstack1111l11ll1l_opy_.bstack11lll111lll_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack1111l11ll1l_opy_.bstack11ll1llllll_opy_()
            if not ordered_test_files:
                return None
            self.bstack11l1l11l_opy_(bstack1lllll1_opy_ (u"ࠤࡸࡴࡱࡵࡡࡥࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡉ࡯ࡶࡰࡷࠦẛ"), len(test_files))
            self.bstack11l1l11l_opy_(bstack1lllll1_opy_ (u"ࠥࡲࡴࡪࡥࡊࡰࡧࡩࡽࠨẜ"), int(os.environ.get(bstack1lllll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡒࡔࡊࡅࡠࡋࡑࡈࡊ࡞ࠢẝ")) or bstack1lllll1_opy_ (u"ࠧ࠶ࠢẞ")))
            self.bstack11l1l11l_opy_(bstack1lllll1_opy_ (u"ࠨࡴࡰࡶࡤࡰࡓࡵࡤࡦࡵࠥẟ"), int(os.environ.get(bstack1lllll1_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖࠥẠ")) or bstack1lllll1_opy_ (u"ࠣ࠳ࠥạ")))
            self.bstack11l1l11l_opy_(bstack1lllll1_opy_ (u"ࠤࡧࡳࡼࡴ࡬ࡰࡣࡧࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳࡄࡱࡸࡲࡹࠨẢ"), len(ordered_test_files))
            self.bstack11l1l11l_opy_(bstack1lllll1_opy_ (u"ࠥࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹࡁࡑࡋࡆࡥࡱࡲࡃࡰࡷࡱࡸࠧả"), self.bstack1111l11ll1l_opy_.bstack11ll1ll1l1l_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡠࡸࡥࡰࡴࡧࡩࡷࡥࡴࡦࡵࡷࡣ࡫࡯࡬ࡦࡵࡠࠤࡊࡸࡲࡰࡴࠣ࡭ࡳࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡣ࡭ࡣࡶࡷࡪࡹ࠺ࠡࡽࢀࠦẤ").format(e))
        return None
    def bstack11l1l11l_opy_(self, key, value):
        self.bstack1111l111l1l_opy_[key] = value
    def bstack111l11ll11_opy_(self):
        return self.bstack1111l111l1l_opy_