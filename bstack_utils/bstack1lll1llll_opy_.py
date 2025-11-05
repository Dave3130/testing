# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import os
from bstack_utils.constants import *
from browserstack_sdk.sdk_cli.cli import cli
from bstack_utils.bstack11ll1l11lll_opy_ import bstack11ll1lll1ll_opy_
from bstack_utils.bstack1lll1l11l_opy_ import bstack111l1l1l_opy_
from bstack_utils.helper import bstack111llll1l_opy_
import json
class bstack1lll1ll11_opy_:
    _1ll1l1lll11_opy_ = None
    def __init__(self, config, logger):
        self.config = config
        self.logger = logger
        self.bstack11111lll1ll_opy_ = bstack11ll1lll1ll_opy_(self.config, logger)
        self.bstack1lll1l11l_opy_ = bstack111l1l1l_opy_.bstack111l1111_opy_(config=self.config)
        self.bstack11111ll1l11_opy_ = {}
        self.bstack11111111_opy_ = False
        self.bstack11111lll111_opy_ = (
            self.__11111ll1lll_opy_()
            and self.bstack1lll1l11l_opy_ is not None
            and self.bstack1lll1l11l_opy_.bstack1111llll_opy_()
            and config.get(bstack1lll11l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫỂ"), None) is not None
            and config.get(bstack1lll11l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪể"), os.path.basename(os.getcwd())) is not None
        )
    @classmethod
    def bstack111l1111_opy_(cls, config, logger):
        if cls._1ll1l1lll11_opy_ is None and config is not None:
            cls._1ll1l1lll11_opy_ = bstack1lll1ll11_opy_(config, logger)
        return cls._1ll1l1lll11_opy_
    def bstack1111llll_opy_(self):
        bstack1lll11l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡊ࡯ࠡࡰࡲࡸࠥࡧࡰࡱ࡮ࡼࠤࡹ࡫ࡳࡵࠢࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡼ࡮ࡥ࡯࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࠭ࠡࡑ࠴࠵ࡾࠦࡩࡴࠢࡱࡳࡹࠦࡥ࡯ࡣࡥࡰࡪࡪࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣ࠱ࠥࡕࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡪࡵࠣࡲࡴࡺࠠࡦࡰࡤࡦࡱ࡫ࡤࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࠲ࠦࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠤ࡮ࡹࠠࡏࡱࡱࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࠯ࠣࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠦࡩࡴࠢࡑࡳࡳ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦỄ")
        return self.bstack11111lll111_opy_ and self.bstack11111llll1l_opy_()
    def bstack11111llll1l_opy_(self):
        bstack11111ll1l1l_opy_ = os.getenv(bstack1lll11l_opy_ (u"ࠩࡉࡖࡆࡓࡅࡘࡑࡕࡏࡤ࡛ࡓࡆࡆࠪễ"), self.config.get(bstack1lll11l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭Ệ"), None))
        return bstack11111ll1l1l_opy_ in bstack11l11llll11_opy_
    def __11111ll1lll_opy_(self):
        bstack11ll11l1ll1_opy_ = False
        for fw in bstack11l1l1111l1_opy_:
            if fw in self.config.get(bstack1lll11l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧệ"), bstack1lll11l_opy_ (u"ࠬ࠭Ỉ")):
                bstack11ll11l1ll1_opy_ = True
        return bstack111llll1l_opy_(self.config.get(bstack1lll11l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡧࡹࡥࡳࡸࡤࡦ࡮ࡲࡩࡵࡻࠪỉ"), bstack11ll11l1ll1_opy_))
    def bstack11111lll1l1_opy_(self):
        return (not self.bstack1111llll_opy_() and
                self.bstack1lll1l11l_opy_ is not None and self.bstack1lll1l11l_opy_.bstack1111llll_opy_())
    def bstack11111ll1ll1_opy_(self):
        if not self.bstack11111lll1l1_opy_():
            return
        if self.config.get(bstack1lll11l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬỊ"), None) is None or self.config.get(bstack1lll11l_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫị"), os.path.basename(os.getcwd())) is None:
            self.logger.info(bstack1lll11l_opy_ (u"ࠤࡗࡩࡸࡺࠠࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡨࡧ࡮ࠨࡶࠣࡻࡴࡸ࡫ࠡࡣࡶࠤࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠠࡰࡴࠣࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠡ࡫ࡶࠤࡳࡻ࡬࡭࠰ࠣࡔࡱ࡫ࡡࡴࡧࠣࡷࡪࡺࠠࡢࠢࡱࡳࡳ࠳࡮ࡶ࡮࡯ࠤࡻࡧ࡬ࡶࡧ࠱ࠦỌ"))
        if not self.__11111ll1lll_opy_():
            self.logger.info(bstack1lll11l_opy_ (u"ࠥࡘࡪࡹࡴࠡࡔࡨࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡩࡡ࡯ࠩࡷࠤࡼࡵࡲ࡬ࠢࡤࡷࠥࡺࡥࡴࡶࡕࡩࡵࡵࡲࡵ࡫ࡱ࡫ࠥ࡯ࡳࠡࡦ࡬ࡷࡦࡨ࡬ࡦࡦ࠱ࠤࡕࡲࡥࡢࡵࡨࠤࡪࡴࡡࡣ࡮ࡨࠤ࡮ࡺࠠࡧࡴࡲࡱࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮࠲ࡾࡳ࡬ࠡࡨ࡬ࡰࡪ࠴ࠢọ"))
    def bstack11111llll11_opy_(self):
        return self.bstack11111111_opy_
    def bstack11l11111_opy_(self, bstack11111lll11l_opy_):
        self.bstack11111111_opy_ = bstack11111lll11l_opy_
        self.bstack1lllll11l_opy_(bstack1lll11l_opy_ (u"ࠦࡦࡶࡰ࡭࡫ࡨࡨࠧỎ"), bstack11111lll11l_opy_)
    def bstack1lllll111_opy_(self, test_files):
        try:
            if test_files is None:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡡࡲࡦࡱࡵࡨࡪࡸ࡟ࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࡡࠥࡔ࡯ࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡶࡲࡰࡸ࡬ࡨࡪࡪࠠࡧࡱࡵࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬࠴ࠢỏ"))
                return None
            orchestration_strategy = None
            orchestration_metadata = self.bstack1lll1l11l_opy_.bstack111lllll1l1_opy_()
            if self.bstack1lll1l11l_opy_ is not None:
                orchestration_strategy = self.bstack1lll1l11l_opy_.bstack11l11l11l1_opy_()
            if orchestration_strategy is None:
                self.logger.error(bstack1lll11l_opy_ (u"ࠨࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡵࡴࡤࡸࡪ࡭ࡹࠡ࡫ࡶࠤࡓࡵ࡮ࡦ࠰ࠣࡇࡦࡴ࡮ࡰࡶࠣࡴࡷࡵࡣࡦࡧࡧࠤࡼ࡯ࡴࡩࠢࡷࡩࡸࡺࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡴࡧࡶࡷ࡮ࡵ࡮࠯ࠤỐ"))
                return None
            self.logger.info(bstack1lll11l_opy_ (u"ࠢࡓࡧࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡹ࡬ࡸ࡭ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡳࡵࡴࡤࡸࡪ࡭ࡹ࠻ࠢࡾࢁࠧố").format(orchestration_strategy))
            if cli.is_running():
                self.logger.debug(bstack1lll11l_opy_ (u"ࠣࡗࡶ࡭ࡳ࡭ࠠࡄࡎࡌࠤ࡫ࡲ࡯ࡸࠢࡩࡳࡷࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠱ࠦỒ"))
                ordered_test_files = cli.test_orchestration_session(test_files, orchestration_strategy, json.dumps(orchestration_metadata))
            else:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠤࡘࡷ࡮ࡴࡧࠡࡵࡧ࡯ࠥ࡬࡬ࡰࡹࠣࡪࡴࡸࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠲ࠧồ"))
                self.bstack11111lll1ll_opy_.bstack11ll1l11ll1_opy_(test_files, orchestration_strategy, orchestration_metadata)
                ordered_test_files = self.bstack11111lll1ll_opy_.bstack11ll1l1l1l1_opy_()
            if not ordered_test_files:
                return None
            self.bstack1lllll11l_opy_(bstack1lll11l_opy_ (u"ࠥࡹࡵࡲ࡯ࡢࡦࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹࡃࡰࡷࡱࡸࠧỔ"), len(test_files))
            self.bstack1lllll11l_opy_(bstack1lll11l_opy_ (u"ࠦࡳࡵࡤࡦࡋࡱࡨࡪࡾࠢổ"), int(os.environ.get(bstack1lll11l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘࠣỖ")) or bstack1lll11l_opy_ (u"ࠨ࠰ࠣỗ")))
            self.bstack1lllll11l_opy_(bstack1lll11l_opy_ (u"ࠢࡵࡱࡷࡥࡱࡔ࡯ࡥࡧࡶࠦỘ"), int(os.environ.get(bstack1lll11l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦộ")) or bstack1lll11l_opy_ (u"ࠤ࠴ࠦỚ")))
            self.bstack1lllll11l_opy_(bstack1lll11l_opy_ (u"ࠥࡨࡴࡽ࡮࡭ࡱࡤࡨࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴࡅࡲࡹࡳࡺࠢớ"), len(ordered_test_files))
            self.bstack1lllll11l_opy_(bstack1lll11l_opy_ (u"ࠦࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳࡂࡒࡌࡇࡦࡲ࡬ࡄࡱࡸࡲࡹࠨỜ"), self.bstack11111lll1ll_opy_.bstack11ll1l1ll1l_opy_())
            return ordered_test_files
        except Exception as e:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡡࡲࡦࡱࡵࡨࡪࡸ࡟ࡵࡧࡶࡸࡤ࡬ࡩ࡭ࡧࡶࡡࠥࡋࡲࡳࡱࡵࠤ࡮ࡴࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡤ࡮ࡤࡷࡸ࡫ࡳ࠻ࠢࡾࢁࠧờ").format(e))
        return None
    def bstack1lllll11l_opy_(self, key, value):
        self.bstack11111ll1l11_opy_[key] = value
    def bstack11lll1111_opy_(self):
        return self.bstack11111ll1l11_opy_