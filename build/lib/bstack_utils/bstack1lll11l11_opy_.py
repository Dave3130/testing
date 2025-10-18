# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1ll1ll1_opy_ import bstack11ll1ll1lll_opy_
from bstack_utils.bstack11111lll_opy_ import bstack111ll1ll_opy_
from bstack_utils.helper import bstack1lll1l1lll_opy_
import json
class bstack1lll1l11l_opy_:
    _1ll1ll1111l_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack11111lll111_opy_ = bstack11ll1ll1lll_opy_(self.config, logger)
        self.bstack11111lll_opy_ = bstack111ll1ll_opy_.bstack11111ll1_opy_(config=self.config)
        self.bstack11111lll1ll_opy_ = {}
        self.bstack1lllll111_opy_ = False
        self.bstack1111l11111l_opy_ = (
            self.__11111llllll_opy_()
            and self.bstack11111lll_opy_ is not None
            and self.bstack11111lll_opy_.bstack1111111l_opy_()
            and config.get(bstack11ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫậ"), None) is not None
            and config.get(bstack11ll_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪẮ"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack11111ll1_opy_(cls, config, logger):
        if cls._1ll1ll1111l_opy_ is None and config is not None:
            cls._1ll1ll1111l_opy_ = bstack1lll1l11l_opy_(config, logger)
        return cls._1ll1ll1111l_opy_
    def bstack1111111l_opy_(self):
        bstack11ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡊ࡯ࠡࡰࡲࡸࠥࡧࡰࡱ࡮ࡼࠤࡹ࡫ࡳࡵࠢࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡼ࡮ࡥ࡯࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡑ࠴࠵ࡾࠦࡩࡴࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡕࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡪࡵࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠦࡩࡴࠢࡑࡳࡳ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦắ")
        return self.bstack1111l11111l_opy_ and self.bstack11111llll11_opy_()
    def bstack11111llll11_opy_(self):
        bstack11111lll11l_opy_ = os.getenv(bstack11ll_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪẰ"), self.config.get(bstack11ll_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ằ"), None))
        return bstack11111lll11l_opy_ in bstack11l1l11lll1_opy_
    def __11111llllll_opy_(self):
        bstack11ll11ll1ll_opy_ = False
        for fw in bstack11l11ll11l1_opy_:
            if fw in self.config.get(bstack11ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧẲ"), bstack11ll_opy_ (u"ࠬ࠭ẳ")):
                bstack11ll11ll1ll_opy_ = True
        return bstack1lll1l1lll_opy_(self.config.get(bstack11ll_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪẴ"), bstack11ll11ll1ll_opy_))
    def bstack11111lll1l1_opy_(self):
        return (not self.bstack1111111l_opy_() and
                self.bstack11111lll_opy_ is not None and self.bstack11111lll_opy_.bstack1111111l_opy_())
    def bstack11111llll1l_opy_(self):
        if not self.bstack11111lll1l1_opy_():
            return
        if self.config.get(bstack11ll_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬẵ"), None) is None or self.config.get(bstack11ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫẶ"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack11ll_opy_ (u"ࠤࡗࡩࡸࡺࠠࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡨࡧ࡮ࠨࡶࠣࡻࡴࡸ࡫ࠡࡣࡶࠤࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠠࡰࡴࠣࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠡ࡫ࡶࠤࡳࡻ࡬࡭࠰ࠣࡔࡱ࡫ࡡࡴࡧࠣࡷࡪࡺࠠࡢࠢࡱࡳࡳ࠳࡮ࡶ࡮࡯ࠤࡻࡧ࡬ࡶࡧ࠱ࠦặ"))
        if not self.__11111llllll_opy_():
            self.logger.info(bstack11ll_opy_ (u"ࠥࡘࡪࡹࡴࠡࡔࡨࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡩࡡ࡯ࠩࡷࠤࡼࡵࡲ࡬ࠢࡤࡷࠥࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡦ࡬ࡷࡦࡨ࡬ࡦࡦ࠱ࠤࡕࡲࡥࡢࡵࡨࠤࡪࡴࡡࡣ࡮ࡨࠤ࡮ࡺࠠࡧࡴࡲࡱࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠡࡨ࡬ࡰࡪ࠴ࠢẸ"))
    def bstack1111l111111_opy_(self):
        return self.bstack1lllll111_opy_
    def bstack111l11l1_opy_(self, bstack11111lllll1_opy_):
        self.bstack1lllll111_opy_ = bstack11111lllll1_opy_
        self.bstack1lllll11l_opy_(bstack11ll_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡨࡨࠧẹ"), bstack11111lllll1_opy_)
    def bstack1lll1ll1l_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack11ll_opy_ (u"ࠧࡡࡲࡦࡱࡵࡨࡪࡸ࡟ࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࡡࠥࡔ࡯ࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡶࡲࡰࡸ࡬ࡨࡪࡪࠠࡧࡱࡵࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬࠴ࠢẺ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack11111lll_opy_.bstack111llll1lll_opy_()
            if self.bstack11111lll_opy_ is not None:
                orchestration_strategy = self.bstack11111lll_opy_.bstack1l111lll11_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack11ll_opy_ (u"ࠨࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡵࡴࡤࡸࡪ࡭ࡹࠡ࡫ࡶࠤࡓࡵ࡮ࡦ࠰ࠣࡇࡦࡴ࡮ࡰࡶࠣࡴࡷࡵࡣࡦࡧࡧࠤࡼ࡯ࡴࡩࠢࡷࡩࡸࡺࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠯ࠤẻ"))
                return None
            self.logger.info(bstack11ll_opy_ (u"ࠢࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡹ࡬ࡸ࡭ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡵࡴࡤࡸࡪ࡭ࡹ࠻ࠢࡾࢁࠧẼ").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack11ll_opy_ (u"ࠣࡗࡶ࡭ࡳ࡭ࠠࡄࡎࡌࠤ࡫ࡲ࡯ࡸࠢࡩࡳࡷࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦẽ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack11ll_opy_ (u"ࠤࡘࡷ࡮ࡴࡧࠡࡵࡧ࡯ࠥ࡬࡬ࡰࡹࠣࡪࡴࡸࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠲ࠧẾ"))
                self.bstack11111lll111_opy_.bstack11lll111111_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack11111lll111_opy_.bstack11ll1l1l1l1_opy_()
            if not ordered_test_files:
                return None
            self.bstack1lllll11l_opy_(bstack11ll_opy_ (u"ࠥࡹࡵࡲ࡯ࡢࡦࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹࡃࡰࡷࡱࡸࠧế"), len(test_files))
            self.bstack1lllll11l_opy_(bstack11ll_opy_ (u"ࠦࡳࡵࡤࡦࡋࡱࡨࡪࡾࠢỀ"), int(os.environ.get(bstack11ll_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘࠣề")) or bstack11ll_opy_ (u"ࠨ࠰ࠣỂ")))
            self.bstack1lllll11l_opy_(bstack11ll_opy_ (u"ࠢࡵࡱࡷࡥࡱࡔ࡯ࡥࡧࡶࠦể"), int(os.environ.get(bstack11ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦỄ")) or bstack11ll_opy_ (u"ࠤ࠴ࠦễ")))
            self.bstack1lllll11l_opy_(bstack11ll_opy_ (u"ࠥࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴࡅࡲࡹࡳࡺࠢỆ"), len(ordered_test_files))
            self.bstack1lllll11l_opy_(bstack11ll_opy_ (u"ࠦࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳࡂࡒࡌࡇࡦࡲ࡬ࡄࡱࡸࡲࡹࠨệ"), self.bstack11111lll111_opy_.bstack11ll1llll11_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack11ll_opy_ (u"ࠧࡡࡲࡦࡱࡵࡨࡪࡸ࡟ࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࡡࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤ࡮ࡤࡷࡸ࡫ࡳ࠻ࠢࡾࢁࠧỈ").format(e))
        return None
    def bstack1lllll11l_opy_(self, key, value):
        self.bstack11111lll1ll_opy_[key] = value
    def bstack1111l1l1ll_opy_(self):
        return self.bstack11111lll1ll_opy_