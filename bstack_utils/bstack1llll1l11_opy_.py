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
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1llll1l_opy_ import bstack11lll1111ll_opy_
from bstack_utils.bstack111lll1l_opy_ import bstack1lll11ll1_opy_
from bstack_utils.helper import bstack111lll11l1_opy_
import json
class bstack1llllll1l_opy_:
    _1ll1ll11111_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack11111llllll_opy_ = bstack11lll1111ll_opy_(self.config, logger)
        self.bstack111lll1l_opy_ = bstack1lll11ll1_opy_.bstack1llll1ll1_opy_(config=self.config)
        self.bstack1111l1111l1_opy_ = {}
        self.bstack111ll1ll_opy_ = False
        self.bstack1111l1111ll_opy_ = (
            self.__1111l111111_opy_()
            and self.bstack111lll1l_opy_ is not None
            and self.bstack111lll1l_opy_.bstack111ll111_opy_()
            and config.get(bstack11l11l1_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫẟ"), None) is not None
            and config.get(bstack11l11l1_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪẠ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack1llll1ll1_opy_(cls, config, logger):
        if cls._1ll1ll11111_opy_ is None and config is not None:
            cls._1ll1ll11111_opy_ = bstack1llllll1l_opy_(config, logger)
        return cls._1ll1ll11111_opy_
    def bstack111ll111_opy_(self):
        bstack11l11l1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡊ࡯ࠡࡰࡲࡸࠥࡧࡰࡱ࡮ࡼࠤࡹ࡫ࡳࡵࠢࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡼ࡮ࡥ࡯࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡑ࠴࠵ࡾࠦࡩࡴࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡕࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡪࡵࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠦࡩࡴࠢࡑࡳࡳ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦạ")
        return self.bstack1111l1111ll_opy_ and self.bstack11111lll1ll_opy_()
    def bstack11111lll1ll_opy_(self):
        bstack11111lllll1_opy_ = os.getenv(bstack11l11l1_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪẢ"), self.config.get(bstack11l11l1_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ả"), None))
        return bstack11111lllll1_opy_ in bstack11l11llll11_opy_
    def __1111l111111_opy_(self):
        bstack11ll11lllll_opy_ = False
        for fw in bstack11l1l11llll_opy_:
            if fw in self.config.get(bstack11l11l1_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧẤ"), bstack11l11l1_opy_ (u"ࠬ࠭ấ")):
                bstack11ll11lllll_opy_ = True
        return bstack111lll11l1_opy_(self.config.get(bstack11l11l1_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪẦ"), bstack11ll11lllll_opy_))
    def bstack1111l111l11_opy_(self):
        return (not self.bstack111ll111_opy_() and
                self.bstack111lll1l_opy_ is not None and self.bstack111lll1l_opy_.bstack111ll111_opy_())
    def bstack11111llll1l_opy_(self):
        if not self.bstack1111l111l11_opy_():
            return
        if self.config.get(bstack11l11l1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬầ"), None) is None or self.config.get(bstack11l11l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫẨ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack11l11l1_opy_ (u"ࠤࡗࡩࡸࡺࠠࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡨࡧ࡮ࠨࡶࠣࡻࡴࡸ࡫ࠡࡣࡶࠤࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠠࡰࡴࠣࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠡ࡫ࡶࠤࡳࡻ࡬࡭࠰ࠣࡔࡱ࡫ࡡࡴࡧࠣࡷࡪࡺࠠࡢࠢࡱࡳࡳ࠳࡮ࡶ࡮࡯ࠤࡻࡧ࡬ࡶࡧ࠱ࠦẩ"))
        if not self.__1111l111111_opy_():
            self.logger.info(bstack11l11l1_opy_ (u"ࠥࡘࡪࡹࡴࠡࡔࡨࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡩࡡ࡯ࠩࡷࠤࡼࡵࡲ࡬ࠢࡤࡷࠥࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡦ࡬ࡷࡦࡨ࡬ࡦࡦ࠱ࠤࡕࡲࡥࡢࡵࡨࠤࡪࡴࡡࡣ࡮ࡨࠤ࡮ࡺࠠࡧࡴࡲࡱࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠡࡨ࡬ࡰࡪ࠴ࠢẪ"))
    def bstack1111l11111l_opy_(self):
        return self.bstack111ll1ll_opy_
    def bstack11111l1l_opy_(self, bstack11111llll11_opy_):
        self.bstack111ll1ll_opy_ = bstack11111llll11_opy_
        self.bstack1111l1ll_opy_(bstack11l11l1_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡨࡨࠧẫ"), bstack11111llll11_opy_)
    def bstack1111111l_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡡࡲࡦࡱࡵࡨࡪࡸ࡟ࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࡡࠥࡔ࡯ࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡶࡲࡰࡸ࡬ࡨࡪࡪࠠࡧࡱࡵࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬࠴ࠢẬ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack111lll1l_opy_.bstack11l1111l111_opy_()
            if self.bstack111lll1l_opy_ is not None:
                orchestration_strategy = self.bstack111lll1l_opy_.bstack1l1lll111l_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack11l11l1_opy_ (u"ࠨࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡵࡴࡤࡸࡪ࡭ࡹࠡ࡫ࡶࠤࡓࡵ࡮ࡦ࠰ࠣࡇࡦࡴ࡮ࡰࡶࠣࡴࡷࡵࡣࡦࡧࡧࠤࡼ࡯ࡴࡩࠢࡷࡩࡸࡺࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠯ࠤậ"))
                return None
            self.logger.info(bstack11l11l1_opy_ (u"ࠢࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡹ࡬ࡸ࡭ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡵࡴࡤࡸࡪ࡭ࡹ࠻ࠢࡾࢁࠧẮ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack11l11l1_opy_ (u"ࠣࡗࡶ࡭ࡳ࡭ࠠࡄࡎࡌࠤ࡫ࡲ࡯ࡸࠢࡩࡳࡷࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦắ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack11l11l1_opy_ (u"ࠤࡘࡷ࡮ࡴࡧࠡࡵࡧ࡯ࠥ࡬࡬ࡰࡹࠣࡪࡴࡸࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠲ࠧẰ"))
                self.bstack11111llllll_opy_.bstack11ll1l1lll1_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack11111llllll_opy_.bstack11ll1lll11l_opy_()
            if not ordered_test_files:
                return None
            self.bstack1111l1ll_opy_(bstack11l11l1_opy_ (u"ࠥࡹࡵࡲ࡯ࡢࡦࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹࡃࡰࡷࡱࡸࠧằ"), len(test_files))
            self.bstack1111l1ll_opy_(bstack11l11l1_opy_ (u"ࠦࡳࡵࡤࡦࡋࡱࡨࡪࡾࠢẲ"), int(os.environ.get(bstack11l11l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘࠣẳ")) or bstack11l11l1_opy_ (u"ࠨ࠰ࠣẴ")))
            self.bstack1111l1ll_opy_(bstack11l11l1_opy_ (u"ࠢࡵࡱࡷࡥࡱࡔ࡯ࡥࡧࡶࠦẵ"), int(os.environ.get(bstack11l11l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦẶ")) or bstack11l11l1_opy_ (u"ࠤ࠴ࠦặ")))
            self.bstack1111l1ll_opy_(bstack11l11l1_opy_ (u"ࠥࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴࡅࡲࡹࡳࡺࠢẸ"), len(ordered_test_files))
            self.bstack1111l1ll_opy_(bstack11l11l1_opy_ (u"ࠦࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳࡂࡒࡌࡇࡦࡲ࡬ࡄࡱࡸࡲࡹࠨẹ"), self.bstack11111llllll_opy_.bstack11lll1111l1_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡡࡲࡦࡱࡵࡨࡪࡸ࡟ࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࡡࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤ࡮ࡤࡷࡸ࡫ࡳ࠻ࠢࡾࢁࠧẺ").format(e))
        return None
    def bstack1111l1ll_opy_(self, key, value):
        self.bstack1111l1111l1_opy_[key] = value
    def bstack1l11l11ll_opy_(self):
        return self.bstack1111l1111l1_opy_