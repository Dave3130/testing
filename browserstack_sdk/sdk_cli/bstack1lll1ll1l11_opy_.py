# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import json
import time
import os
import threading
import asyncio
from browserstack_sdk.sdk_cli.bstack1llll1ll111_opy_ import (
    bstack1lllllll1l1_opy_,
    bstack1llllll1l11_opy_,
    bstack1lllll111l1_opy_,
    bstack1lll1ll1l1l_opy_,
)
from typing import Tuple, Dict, Any, List, Union
from bstack_utils.helper import bstack1lll1ll11ll_opy_, bstack11l1ll11l1_opy_
from browserstack_sdk.sdk_cli.bstack1llll11l1ll_opy_ import bstack1llll1lllll_opy_
from browserstack_sdk.sdk_cli.test_framework import TestFramework, bstack1llll111l1l_opy_, bstack1lll1lll111_opy_, bstack1lll1l1llll_opy_
from browserstack_sdk.sdk_cli.bstack1lll1ll1lll_opy_ import bstack1lll1l1l1ll_opy_
from browserstack_sdk.sdk_cli.bstack1lll11ll1ll_opy_ import bstack1lll1lll1l1_opy_
from typing import Tuple, List, Any
from bstack_utils.bstack1l1ll111l1_opy_ import bstack111lll1l11_opy_, bstack1l1ll1l11_opy_, bstack1l1ll111ll_opy_
from browserstack_sdk import sdk_pb2 as structs
class bstack1lll11l1lll_opy_(bstack1lll1lll1l1_opy_):
    bstack1lll1l1lll1_opy_ = bstack1lllll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡡࡧࡶ࡮ࡼࡥࡳࡵࠥᄢ")
    bstack1lll1ll1ll1_opy_ = bstack1lllll1l_opy_ (u"ࠧࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡶࠦᄣ")
    bstack1lll11llll1_opy_ = bstack1lllll1l_opy_ (u"ࠨ࡮ࡰࡰࡢࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࡡࡤࡹࡹࡵ࡭ࡢࡶ࡬ࡳࡳࡥࡳࡦࡵࡶ࡭ࡴࡴࡳࠣᄤ")
    bstack1lll1ll11l1_opy_ = bstack1lllll1l_opy_ (u"ࠢࡵࡧࡶࡸࡤࡹࡥࡴࡵ࡬ࡳࡳࡹࠢᄥ")
    bstack1llll111111_opy_ = bstack1lllll1l_opy_ (u"ࠣࡣࡸࡸࡴࡳࡡࡵ࡫ࡲࡲࡤ࡯࡮ࡴࡶࡤࡲࡨ࡫࡟ࡳࡧࡩࡷࠧᄦ")
    bstack1lll1l11lll_opy_ = bstack1lllll1l_opy_ (u"ࠤࡦࡦࡹࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡤࡴࡨࡥࡹ࡫ࡤࠣᄧ")
    bstack1lll11ll11l_opy_ = bstack1lllll1l_opy_ (u"ࠥࡧࡧࡺ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠࡰࡤࡱࡪࠨᄨ")
    bstack1llll11l111_opy_ = bstack1lllll1l_opy_ (u"ࠦࡨࡨࡴࡠࡵࡨࡷࡸ࡯࡯࡯ࡡࡶࡸࡦࡺࡵࡴࠤᄩ")
    def __init__(self):
        super().__init__(bstack1llll1111ll_opy_=self.bstack1lll1l1lll1_opy_, frameworks=[bstack1llll1lllll_opy_.NAME])
        if not self.is_enabled():
            return
        TestFramework.bstack1llll1l1l11_opy_((bstack1llll111l1l_opy_.BEFORE_EACH, bstack1lll1lll111_opy_.POST), self.bstack1lll1l11111_opy_)
        if bstack11l1ll11l1_opy_():
            TestFramework.bstack1llll1l1l11_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.POST), self.bstack1lll1ll1111_opy_)
        else:
            TestFramework.bstack1llll1l1l11_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.PRE), self.bstack1lll1ll1111_opy_)
        TestFramework.bstack1llll1l1l11_opy_((bstack1llll111l1l_opy_.TEST, bstack1lll1lll111_opy_.POST), self.bstack1lll1l11l11_opy_)
    def is_enabled(self) -> bool:
        return True
    def bstack1lll1l11111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        bstack1lll11lll1l_opy_ = self.bstack1lll1l1ll1l_opy_(instance.context)
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡹࡥࡵࡡࡤࡧࡹ࡯ࡶࡦࡡࡳࡥ࡬࡫࠺ࠡࡰࡲࠤࡵࡧࡧࡦࠢࡩࡳࡷࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥᄪ") + str(bstack1llll1l1lll_opy_) + bstack1lllll1l_opy_ (u"ࠨࠢᄫ"))
            return
        f.bstack1llll11ll1l_opy_(instance, bstack1lll11l1lll_opy_.bstack1lll1ll1ll1_opy_, bstack1lll11lll1l_opy_)
    def bstack1lll1l1ll1l_opy_(self, context: bstack1lll1ll1l1l_opy_, bstack1lll1l1l1l1_opy_= True):
        if bstack1lll1l1l1l1_opy_:
            bstack1lll11lll1l_opy_ = self.bstack1llll1111l1_opy_(context, reverse=True)
        else:
            bstack1lll11lll1l_opy_ = self.bstack1lll1ll111l_opy_(context, reverse=True)
        return [f for f in bstack1lll11lll1l_opy_ if f[1].state != bstack1lllllll1l1_opy_.QUIT]
    def bstack1lll1ll1111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l11111_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        if not bstack1lll1ll11ll_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄬ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠣࠤᄭ"))
            return
        bstack1lll11lll1l_opy_ = f.get_state(instance, bstack1lll11l1lll_opy_.bstack1lll1ll1ll1_opy_, [])
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄮ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠥࠦᄯ"))
            return
        if len(bstack1lll11lll1l_opy_) > 1:
            self.logger.debug(
                bstack11ll1l1l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡵࡧࡧࡦࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨᄰ"))
        bstack1llll111lll_opy_, bstack1lll1l1l11l_opy_ = bstack1lll11lll1l_opy_[0]
        page = bstack1llll111lll_opy_()
        if not page:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄱ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠨࠢᄲ"))
            return
        bstack11lll11l1l_opy_ = getattr(args[0], bstack1lllll1l_opy_ (u"ࠢ࡯ࡱࡧࡩ࡮ࡪࠢᄳ"), None)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1lllll1l_opy_ (u"ࠣࡶࡨࡷࡹࡉ࡯࡯ࡶࡨࡼࡹࡕࡰࡵ࡫ࡲࡲࡸࠨᄴ")).get(bstack1lllll1l_opy_ (u"ࠤࡶ࡯࡮ࡶࡓࡦࡵࡶ࡭ࡴࡴࡎࡢ࡯ࡨࠦᄵ")):
            try:
                page.evaluate(bstack1lllll1l_opy_ (u"ࠥࡣࠥࡃ࠾ࠡࡽࢀࠦᄶ"),
                            bstack1lllll1l_opy_ (u"ࠫࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࡢࡩࡽ࡫ࡣࡶࡶࡲࡶ࠿ࠦࡻࠣࡣࡦࡸ࡮ࡵ࡮ࠣ࠼ࠣࠦࡸ࡫ࡴࡔࡧࡶࡷ࡮ࡵ࡮ࡏࡣࡰࡩࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࡻࠣࡰࡤࡱࡪࠨ࠺ࠨᄷ") + json.dumps(
                                bstack11lll11l1l_opy_) + bstack1lllll1l_opy_ (u"ࠧࢃࡽࠣᄸ"))
            except Exception as e:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠨࡥࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠢࡶࡩࡸࡹࡩࡰࡰࠣࡲࡦࡳࡥࠡࡽࢀࠦᄹ"), e)
    def bstack1lll1l11l11_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l11111_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        if not bstack1lll1ll11ll_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢࡰࡰࡢࡦࡪ࡬࡯ࡳࡧࡢࡸࡪࡹࡴ࠻ࠢࡱࡳࡹࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠥࡹࡥࡴࡵ࡬ࡳࡳࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᄺ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠣࠤᄻ"))
            return
        bstack1lll11lll1l_opy_ = f.get_state(instance, bstack1lll11l1lll_opy_.bstack1lll1ll1ll1_opy_, [])
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡲࡲࡤࡨࡥࡧࡱࡵࡩࡤࡺࡥࡴࡶ࠽ࠤࡳࡵࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄼ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠥࠦᄽ"))
            return
        if len(bstack1lll11lll1l_opy_) > 1:
            self.logger.debug(
                bstack11ll1l1l_opy_ (u"ࠦࡴࡴ࡟ࡣࡧࡩࡳࡷ࡫࡟ࡵࡧࡶࡸ࠿ࠦࡻ࡭ࡧࡱࠬࡵࡧࡧࡦࡡ࡬ࡲࡸࡺࡡ࡯ࡥࡨࡷ࠮ࢃࠠࡥࡴ࡬ࡺࡪࡸࡳࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨᄾ"))
        bstack1llll111lll_opy_, bstack1lll1l1l11l_opy_ = bstack1lll11lll1l_opy_[0]
        page = bstack1llll111lll_opy_()
        if not page:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡵ࡮ࡠࡤࡨࡪࡴࡸࡥࡠࡶࡨࡷࡹࡀࠠ࡯ࡱࠣࡴࡦ࡭ࡥࠡࡨࡲࡶࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࠧᄿ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠨࠢᅀ"))
            return
        status = f.get_state(instance, TestFramework.bstack1lll1l1111l_opy_, None)
        if not status:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠢ࡯ࡱࠣࡷࡹࡧࡴࡶࡵࠣࡪࡴࡸࠠࡵࡧࡶࡸ࠱ࠦࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰ࠿ࠥᅁ") + str(bstack1llll1l1lll_opy_) + bstack1lllll1l_opy_ (u"ࠣࠤᅂ"))
            return
        bstack1lll11ll1l1_opy_ = {bstack1lllll1l_opy_ (u"ࠤࡶࡸࡦࡺࡵࡴࠤᅃ"): status.lower()}
        bstack1lll1llllll_opy_ = f.get_state(instance, TestFramework.bstack1lll11ll111_opy_, None)
        if status.lower() == bstack1lllll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᅄ") and bstack1lll1llllll_opy_ is not None:
            bstack1lll11ll1l1_opy_[bstack1lllll1l_opy_ (u"ࠫࡷ࡫ࡡࡴࡱࡱࠫᅅ")] = bstack1lll1llllll_opy_[0][bstack1lllll1l_opy_ (u"ࠬࡨࡡࡤ࡭ࡷࡶࡦࡩࡥࠨᅆ")][0] if isinstance(bstack1lll1llllll_opy_, list) else str(bstack1lll1llllll_opy_)
        from browserstack_sdk.sdk_cli.cli import cli
        if not cli.config.get(bstack1lllll1l_opy_ (u"ࠨࡴࡦࡵࡷࡇࡴࡴࡴࡦࡺࡷࡓࡵࡺࡩࡰࡰࡶࠦᅇ")).get(bstack1lllll1l_opy_ (u"ࠢࡴ࡭࡬ࡴࡘ࡫ࡳࡴ࡫ࡲࡲࡘࡺࡡࡵࡷࡶࠦᅈ")):
            try:
                page.evaluate(
                        bstack1lllll1l_opy_ (u"ࠣࡡࠣࡁࡃࠦࡻࡾࠤᅉ"),
                        bstack1lllll1l_opy_ (u"ࠩࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࡠࡧࡻࡩࡨࡻࡴࡰࡴ࠽ࠤࢀࠨࡡࡤࡶ࡬ࡳࡳࠨ࠺ࠡࠤࡶࡩࡹ࡙ࡥࡴࡵ࡬ࡳࡳ࡙ࡴࡢࡶࡸࡷࠧ࠲ࠠࠣࡣࡵ࡫ࡺࡳࡥ࡯ࡶࡶࠦ࠿ࠦࠧᅊ")
                        + json.dumps(bstack1lll11ll1l1_opy_)
                        + bstack1lllll1l_opy_ (u"ࠥࢁࠧᅋ")
                    )
            except Exception as e:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡪࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠠࡴࡧࡶࡷ࡮ࡵ࡮ࠡࡵࡷࡥࡹࡻࡳࠡࡽࢀࠦᅌ"), e)
    def bstack1lll1l11ll1_opy_(
        self,
        instance: bstack1lll1l1llll_opy_,
        f: TestFramework,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l11111_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        if not bstack1lll1ll11ll_opy_:
            self.logger.debug(
                bstack11ll1l1l_opy_ (u"ࠧࡳࡡࡳ࡭ࡢࡳ࠶࠷ࡹࡠࡵࡼࡲࡨࡀࠠ࡯ࡱࡷࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠣࡷࡪࡹࡳࡪࡱࡱ࠰ࠥ࡮࡯ࡰ࡭ࡢ࡭ࡳ࡬࡯࠾ࡽ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࢂࠦࡡࡳࡩࡶࡁࢀࡧࡲࡨࡵࢀࠤࡰࡽࡡࡳࡩࡶࡁࢀࡱࡷࡢࡴࡪࡷࢂࠨᅍ"))
            return
        bstack1lll11lll1l_opy_ = f.get_state(instance, bstack1lll11l1lll_opy_.bstack1lll1ll1ll1_opy_, [])
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠨ࡯࡯ࡡࡥࡩ࡫ࡵࡲࡦࡡࡷࡩࡸࡺ࠺ࠡࡰࡲࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᅎ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠢࠣᅏ"))
            return
        if len(bstack1lll11lll1l_opy_) > 1:
            self.logger.debug(
                bstack11ll1l1l_opy_ (u"ࠣࡱࡱࡣࡧ࡫ࡦࡰࡴࡨࡣࡹ࡫ࡳࡵ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࡽ࡮ࡻࡦࡸࡧࡴࡿࠥᅐ"))
        bstack1llll111lll_opy_, bstack1lll1l1l11l_opy_ = bstack1lll11lll1l_opy_[0]
        page = bstack1llll111lll_opy_()
        if not page:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠤࡰࡥࡷࡱ࡟ࡰ࠳࠴ࡽࡤࡹࡹ࡯ࡥ࠽ࠤࡳࡵࠠࡱࡣࡪࡩࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᅑ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠥࠦᅒ"))
            return
        timestamp = int(time.time() * 1000)
        data = bstack1lllll1l_opy_ (u"ࠦࡔࡨࡳࡦࡴࡹࡥࡧ࡯࡬ࡪࡶࡼࡗࡾࡴࡣ࠻ࠤᅓ") + str(timestamp)
        try:
            page.evaluate(
                bstack1lllll1l_opy_ (u"ࠧࡥࠠ࠾ࡀࠣࡿࢂࠨᅔ"),
                bstack1lllll1l_opy_ (u"࠭ࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࡤ࡫ࡸࡦࡥࡸࡸࡴࡸ࠺ࠡࡽࢀࠫᅕ").format(
                    json.dumps(
                        {
                            bstack1lllll1l_opy_ (u"ࠢࡢࡥࡷ࡭ࡴࡴࠢᅖ"): bstack1lllll1l_opy_ (u"ࠣࡣࡱࡲࡴࡺࡡࡵࡧࠥᅗ"),
                            bstack1lllll1l_opy_ (u"ࠤࡤࡶ࡬ࡻ࡭ࡦࡰࡷࡷࠧᅘ"): {
                                bstack1lllll1l_opy_ (u"ࠥࡸࡾࡶࡥࠣᅙ"): bstack1lllll1l_opy_ (u"ࠦࡆࡴ࡮ࡰࡶࡤࡸ࡮ࡵ࡮ࠣᅚ"),
                                bstack1lllll1l_opy_ (u"ࠧࡪࡡࡵࡣࠥᅛ"): data,
                                bstack1lllll1l_opy_ (u"ࠨ࡬ࡦࡸࡨࡰࠧᅜ"): bstack1lllll1l_opy_ (u"ࠢࡥࡧࡥࡹ࡬ࠨᅝ")
                            }
                        }
                    )
                )
            )
        except Exception as e:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡧࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠤࡴ࠷࠱ࡺࠢࡤࡲࡳࡵࡴࡢࡶ࡬ࡳࡳࠦ࡭ࡢࡴ࡮࡭ࡳ࡭ࠠࡼࡿࠥᅞ"), e)
    def bstack1lll1l11l1l_opy_(
        self,
        instance: bstack1lll1l1llll_opy_,
        f: TestFramework,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs,
    ):
        self.bstack1lll1l11111_opy_(f, instance, bstack1llll1l1lll_opy_, *args, **kwargs)
        if f.get_state(instance, bstack1lll11l1lll_opy_.bstack1lll1l11lll_opy_, False):
            return
        self.bstack1llll1lll11_opy_()
        req = structs.TestSessionEventRequest()
        req.bin_session_id = self.bin_session_id
        req.platform_index = TestFramework.get_state(instance, TestFramework.bstack1llllllllll_opy_)
        req.test_framework_name = TestFramework.get_state(instance, TestFramework.bstack1lll1l111l1_opy_)
        req.test_framework_version = TestFramework.get_state(instance, TestFramework.bstack1lll11lll11_opy_)
        req.test_framework_state = bstack1llll1l1lll_opy_[0].name
        req.test_hook_state = bstack1llll1l1lll_opy_[1].name
        req.test_uuid = TestFramework.get_state(instance, TestFramework.bstack1lll1lll1ll_opy_)
        for bstack1lll1llll11_opy_ in bstack1lll1l1l1ll_opy_.bstack1lll11lllll_opy_.values():
            session = req.automation_sessions.add()
            session.provider = (
                bstack1lllll1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠣᅟ")
                if bstack1lll1ll11ll_opy_
                else bstack1lllll1l_opy_ (u"ࠥࡹࡳࡱ࡮ࡰࡹࡱࡣ࡬ࡸࡩࡥࠤᅠ")
            )
            session.ref = bstack1lll1llll11_opy_.ref()
            session.hub_url = bstack1lll1l1l1ll_opy_.get_state(bstack1lll1llll11_opy_, bstack1lll1l1l1ll_opy_.bstack1lll1lllll1_opy_, bstack1lllll1l_opy_ (u"ࠦࠧᅡ"))
            session.framework_name = bstack1lll1llll11_opy_.framework_name
            session.framework_version = bstack1lll1llll11_opy_.framework_version
            session.framework_session_id = bstack1lll1l1l1ll_opy_.get_state(bstack1lll1llll11_opy_, bstack1lll1l1l1ll_opy_.bstack1lll1llll1l_opy_, bstack1lllll1l_opy_ (u"ࠧࠨᅢ"))
        req.execution_context.hash = str(instance.context.hash)
        req.execution_context.thread_id = str(instance.context.thread_id)
        req.execution_context.process_id = str(instance.context.process_id)
        return req
    def bstack1lll1l1l111_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs
    ):
        bstack1lll11lll1l_opy_ = f.get_state(instance, bstack1lll11l1lll_opy_.bstack1lll1ll1ll1_opy_, [])
        if not bstack1lll11lll1l_opy_:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠨࡧࡦࡶࡢࡥࡺࡺ࡯࡮ࡣࡷ࡭ࡴࡴ࡟ࡥࡴ࡬ࡺࡪࡸ࠺ࠡࡰࡲࠤࡵࡧࡧࡦࡵࠣࡪࡴࡸࠠࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࡀࡿ࡭ࡵ࡯࡬ࡡ࡬ࡲ࡫ࡵࡽࠡࡣࡵ࡫ࡸࡃࡻࡢࡴࡪࡷࢂࠦ࡫ࡸࡣࡵ࡫ࡸࡃࠢᅣ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠢࠣᅤ"))
            return
        if len(bstack1lll11lll1l_opy_) > 1:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠣࡩࡨࡸࡤࡧࡵࡵࡱࡰࡥࡹ࡯࡯࡯ࡡࡧࡶ࡮ࡼࡥࡳ࠼ࠣࡿࡱ࡫࡮ࠩࡲࡤ࡫ࡪࡥࡩ࡯ࡵࡷࡥࡳࡩࡥࡴࠫࢀࠤࡩࡸࡩࡷࡧࡵࡷࠥ࡬࡯ࡳࠢ࡫ࡳࡴࡱ࡟ࡪࡰࡩࡳࡂࢁࡨࡰࡱ࡮ࡣ࡮ࡴࡦࡰࡿࠣࡥࡷ࡭ࡳ࠾ࡽࡤࡶ࡬ࡹࡽࠡ࡭ࡺࡥࡷ࡭ࡳ࠾ࠤᅥ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠤࠥᅦ"))
        bstack1llll111lll_opy_, bstack1lll1l1l11l_opy_ = bstack1lll11lll1l_opy_[0]
        page = bstack1llll111lll_opy_()
        if not page:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠥ࡫ࡪࡺ࡟ࡢࡷࡷࡳࡲࡧࡴࡪࡱࡱࡣࡩࡸࡩࡷࡧࡵ࠾ࠥࡴ࡯ࠡࡲࡤ࡫ࡪࠦࡦࡰࡴࠣ࡬ࡴࡵ࡫ࡠ࡫ࡱࡪࡴࡃࡻࡩࡱࡲ࡯ࡤ࡯࡮ࡧࡱࢀࠤࡦࡸࡧࡴ࠿ࡾࡥࡷ࡭ࡳࡾࠢ࡮ࡻࡦࡸࡧࡴ࠿ࠥᅧ") + str(kwargs) + bstack1lllll1l_opy_ (u"ࠦࠧᅨ"))
            return
        return page
    def bstack1lll1l111ll_opy_(
        self,
        f: TestFramework,
        instance: bstack1lll1l1llll_opy_,
        bstack1llll1l1lll_opy_: Tuple[bstack1llll111l1l_opy_, bstack1lll1lll111_opy_],
        *args,
        **kwargs
    ):
        caps = {}
        bstack1llll111ll1_opy_ = {}
        for bstack1lll1llll11_opy_ in bstack1lll1l1l1ll_opy_.bstack1lll11lllll_opy_.values():
            caps = bstack1lll1l1l1ll_opy_.get_state(bstack1lll1llll11_opy_, bstack1lll1l1l1ll_opy_.bstack1llll111l11_opy_, bstack1lllll1l_opy_ (u"ࠧࠨᅩ"))
        bstack1llll111ll1_opy_[bstack1lllll1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦᅪ")] = caps.get(bstack1lllll1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࠣᅫ"), bstack1lllll1l_opy_ (u"ࠣࠤᅬ"))
        bstack1llll111ll1_opy_[bstack1lllll1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣᅭ")] = caps.get(bstack1lllll1l_opy_ (u"ࠥࡳࡸࠨᅮ"), bstack1lllll1l_opy_ (u"ࠦࠧᅯ"))
        bstack1llll111ll1_opy_[bstack1lllll1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢᅰ")] = caps.get(bstack1lllll1l_opy_ (u"ࠨ࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠥᅱ"), bstack1lllll1l_opy_ (u"ࠢࠣᅲ"))
        bstack1llll111ll1_opy_[bstack1lllll1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤᅳ")] = caps.get(bstack1lllll1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠦᅴ"), bstack1lllll1l_opy_ (u"ࠥࠦᅵ"))
        return bstack1llll111ll1_opy_
    def bstack1llll11111l_opy_(self, page: object, bstack1lll1lll11l_opy_, args={}):
        try:
            bstack1lll1l1ll11_opy_ = bstack1lllll1l_opy_ (u"ࠦࠧࠨࠨࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࠫ࠲࠳࠴ࡢࡴࡶࡤࡧࡰ࡙ࡤ࡬ࡃࡵ࡫ࡸ࠯ࠠࡼࡽࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡸࡥࡵࡷࡵࡲࠥࡴࡥࡸࠢࡓࡶࡴࡳࡩࡴࡧࠫࠬࡷ࡫ࡳࡰ࡮ࡹࡩ࠱ࠦࡲࡦ࡬ࡨࡧࡹ࠯ࠠ࠾ࡀࠣࡿࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡳࡵࡣࡦ࡯ࡘࡪ࡫ࡂࡴࡪࡷ࠳ࡶࡵࡴࡪࠫࡶࡪࡹ࡯࡭ࡸࡨ࠭ࡀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࢁࡦ࡯ࡡࡥࡳࡩࡿࡽࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࢁࢂ࠯࠻ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡽࡾࠫࠫࡿࡦࡸࡧࡠ࡬ࡶࡳࡳࢃࠩࠣࠤࠥᅶ")
            bstack1lll1lll11l_opy_ = bstack1lll1lll11l_opy_.replace(bstack1lllll1l_opy_ (u"ࠧࡧࡲࡨࡷࡰࡩࡳࡺࡳࠣᅷ"), bstack1lllll1l_opy_ (u"ࠨࡢࡴࡶࡤࡧࡰ࡙ࡤ࡬ࡃࡵ࡫ࡸࠨᅸ"))
            script = bstack1lll1l1ll11_opy_.format(fn_body=bstack1lll1lll11l_opy_, arg_json=json.dumps(args))
            return page.evaluate(script)
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠢࡢ࠳࠴ࡽࡤࡹࡣࡳ࡫ࡳࡸࡤ࡫ࡸࡦࡥࡸࡸࡪࡀࠠࡆࡴࡵࡳࡷࠦࡥࡹࡧࡦࡹࡹ࡯࡮ࡨࠢࡷ࡬ࡪࠦࡡ࠲࠳ࡼࠤࡸࡩࡲࡪࡲࡷ࠰ࠥࠨᅹ") + str(e) + bstack1lllll1l_opy_ (u"ࠣࠤᅺ"))