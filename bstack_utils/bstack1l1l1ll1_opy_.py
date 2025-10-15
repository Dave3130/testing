# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
from uuid import uuid4
from bstack_utils.helper import bstack1l1l1lll_opy_, bstack1111ll1ll1l_opy_
from bstack_utils.bstack1l111l1l1_opy_ import bstack11l11l11111_opy_
class bstack1ll1llll_opy_:
    def __init__(self, name=None, code=None, uuid=None, file_path=None, started_at=None, framework=None, tags=[], scope=[], bstack111111llll1_opy_=None, bstack11111l1l11l_opy_=True, bstack1ll1l1l1lll_opy_=None, bstack11llll1ll1_opy_=None, result=None, duration=None, bstack1l11ll1l_opy_=None, meta={}):
        self.bstack1l11ll1l_opy_ = bstack1l11ll1l_opy_
        self.name = name
        self.code = code
        self.file_path = file_path
        self.uuid = uuid
        if not self.uuid and bstack11111l1l11l_opy_:
            self.uuid = uuid4().__str__()
        self.started_at = started_at
        self.framework = framework
        self.tags = tags
        self.scope = scope
        self.bstack111111llll1_opy_ = bstack111111llll1_opy_
        self.bstack1ll1l1l1lll_opy_ = bstack1ll1l1l1lll_opy_
        self.bstack11llll1ll1_opy_ = bstack11llll1ll1_opy_
        self.result = result
        self.duration = duration
        self.meta = meta
        self.hooks = []
    def bstack1l1ll1l1_opy_(self):
        if self.uuid:
            return self.uuid
        self.uuid = uuid4().__str__()
        return self.uuid
    def bstack11ll11ll_opy_(self, meta):
        self.meta = meta
    def bstack11l1lll1_opy_(self, hooks):
        self.hooks = hooks
    def bstack11111l1l1l1_opy_(self):
        bstack11111l11lll_opy_ = os.path.relpath(self.file_path, start=os.getcwd())
        return {
            bstack1ll1l_opy_ (u"ࠪࡪ࡮ࡲࡥࡠࡰࡤࡱࡪ࠭Ợ"): bstack11111l11lll_opy_,
            bstack1ll1l_opy_ (u"ࠫࡱࡵࡣࡢࡶ࡬ࡳࡳ࠭ợ"): bstack11111l11lll_opy_,
            bstack1ll1l_opy_ (u"ࠬࡼࡣࡠࡨ࡬ࡰࡪࡶࡡࡵࡪࠪỤ"): bstack11111l11lll_opy_
        }
    def set(self, **kwargs):
        for key, val in kwargs.items():
            if not hasattr(self, key):
                raise TypeError(bstack1ll1l_opy_ (u"ࠨࡕ࡯ࡧࡻࡴࡪࡩࡴࡦࡦࠣࡥࡷ࡭ࡵ࡮ࡧࡱࡸ࠿ࠦࠢụ") + key)
            setattr(self, key, val)
    def bstack111111lll1l_opy_(self):
        return {
            bstack1ll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬỦ"): self.name,
            bstack1ll1l_opy_ (u"ࠨࡤࡲࡨࡾ࠭ủ"): {
                bstack1ll1l_opy_ (u"ࠩ࡯ࡥࡳ࡭ࠧỨ"): bstack1ll1l_opy_ (u"ࠪࡴࡾࡺࡨࡰࡰࠪứ"),
                bstack1ll1l_opy_ (u"ࠫࡨࡵࡤࡦࠩỪ"): self.code
            },
            bstack1ll1l_opy_ (u"ࠬࡹࡣࡰࡲࡨࡷࠬừ"): self.scope,
            bstack1ll1l_opy_ (u"࠭ࡴࡢࡩࡶࠫỬ"): self.tags,
            bstack1ll1l_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪử"): self.framework,
            bstack1ll1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬỮ"): self.started_at
        }
    def bstack11111l111l1_opy_(self):
        return {
         bstack1ll1l_opy_ (u"ࠩࡰࡩࡹࡧࠧữ"): self.meta
        }
    def bstack11111l11l1l_opy_(self):
        return {
            bstack1ll1l_opy_ (u"ࠪࡧࡺࡹࡴࡰ࡯ࡕࡩࡷࡻ࡮ࡑࡣࡵࡥࡲ࠭Ự"): {
                bstack1ll1l_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡢࡲࡦࡳࡥࠨự"): self.bstack111111llll1_opy_
            }
        }
    def bstack11111l1l111_opy_(self, bstack111111ll1l1_opy_, details):
        step = next(filter(lambda st: st[bstack1ll1l_opy_ (u"ࠬ࡯ࡤࠨỲ")] == bstack111111ll1l1_opy_, self.meta[bstack1ll1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬỳ")]), None)
        step.update(details)
    def bstack11l1ll1l_opy_(self, bstack111111ll1l1_opy_):
        step = next(filter(lambda st: st[bstack1ll1l_opy_ (u"ࠧࡪࡦࠪỴ")] == bstack111111ll1l1_opy_, self.meta[bstack1ll1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧỵ")]), None)
        step.update({
            bstack1ll1l_opy_ (u"ࠩࡶࡸࡦࡸࡴࡦࡦࡢࡥࡹ࠭Ỷ"): bstack1l1l1lll_opy_()
        })
    def bstack1ll1l111_opy_(self, bstack111111ll1l1_opy_, result, duration=None):
        bstack1ll1l1l1lll_opy_ = bstack1l1l1lll_opy_()
        if bstack111111ll1l1_opy_ is not None and self.meta.get(bstack1ll1l_opy_ (u"ࠪࡷࡹ࡫ࡰࡴࠩỷ")):
            step = next(filter(lambda st: st[bstack1ll1l_opy_ (u"ࠫ࡮ࡪࠧỸ")] == bstack111111ll1l1_opy_, self.meta[bstack1ll1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫỹ")]), None)
            step.update({
                bstack1ll1l_opy_ (u"࠭ࡦࡪࡰ࡬ࡷ࡭࡫ࡤࡠࡣࡷࠫỺ"): bstack1ll1l1l1lll_opy_,
                bstack1ll1l_opy_ (u"ࠧࡥࡷࡵࡥࡹ࡯࡯࡯ࠩỻ"): duration if duration else bstack1111ll1ll1l_opy_(step[bstack1ll1l_opy_ (u"ࠨࡵࡷࡥࡷࡺࡥࡥࡡࡤࡸࠬỼ")], bstack1ll1l1l1lll_opy_),
                bstack1ll1l_opy_ (u"ࠩࡵࡩࡸࡻ࡬ࡵࠩỽ"): result.result,
                bstack1ll1l_opy_ (u"ࠪࡪࡦ࡯࡬ࡶࡴࡨࠫỾ"): str(result.exception) if result.exception else None
            })
    def add_step(self, bstack11111l111ll_opy_):
        if self.meta.get(bstack1ll1l_opy_ (u"ࠫࡸࡺࡥࡱࡵࠪỿ")):
            self.meta[bstack1ll1l_opy_ (u"ࠬࡹࡴࡦࡲࡶࠫἀ")].append(bstack11111l111ll_opy_)
        else:
            self.meta[bstack1ll1l_opy_ (u"࠭ࡳࡵࡧࡳࡷࠬἁ")] = [ bstack11111l111ll_opy_ ]
    def bstack11111l1111l_opy_(self):
        return {
            bstack1ll1l_opy_ (u"ࠧࡶࡷ࡬ࡨࠬἂ"): self.bstack1l1ll1l1_opy_(),
            **self.bstack111111lll1l_opy_(),
            **self.bstack11111l1l1l1_opy_(),
            **self.bstack11111l111l1_opy_()
        }
    def bstack11111l11ll1_opy_(self):
        if not self.result:
            return {}
        data = {
            bstack1ll1l_opy_ (u"ࠨࡨ࡬ࡲ࡮ࡹࡨࡦࡦࡢࡥࡹ࠭ἃ"): self.bstack1ll1l1l1lll_opy_,
            bstack1ll1l_opy_ (u"ࠩࡧࡹࡷࡧࡴࡪࡱࡱࡣ࡮ࡴ࡟࡮ࡵࠪἄ"): self.duration,
            bstack1ll1l_opy_ (u"ࠪࡶࡪࡹࡵ࡭ࡶࠪἅ"): self.result.result
        }
        if data[bstack1ll1l_opy_ (u"ࠫࡷ࡫ࡳࡶ࡮ࡷࠫἆ")] == bstack1ll1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬἇ"):
            data[bstack1ll1l_opy_ (u"࠭ࡦࡢ࡫࡯ࡹࡷ࡫࡟ࡵࡻࡳࡩࠬἈ")] = self.result.bstack11111l11l1_opy_()
            data[bstack1ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡺࡸࡥࠨἉ")] = [{bstack1ll1l_opy_ (u"ࠨࡤࡤࡧࡰࡺࡲࡢࡥࡨࠫἊ"): self.result.bstack111l11lllll_opy_()}]
        return data
    def bstack111111ll1ll_opy_(self):
        return {
            bstack1ll1l_opy_ (u"ࠩࡸࡹ࡮ࡪࠧἋ"): self.bstack1l1ll1l1_opy_(),
            **self.bstack111111lll1l_opy_(),
            **self.bstack11111l1l1l1_opy_(),
            **self.bstack11111l11ll1_opy_(),
            **self.bstack11111l111l1_opy_()
        }
    def bstack1llll1ll_opy_(self, event, result=None):
        if result:
            self.result = result
        if bstack1ll1l_opy_ (u"ࠪࡗࡹࡧࡲࡵࡧࡧࠫἌ") in event:
            return self.bstack11111l1111l_opy_()
        elif bstack1ll1l_opy_ (u"ࠫࡋ࡯࡮ࡪࡵ࡫ࡩࡩ࠭Ἅ") in event:
            return self.bstack111111ll1ll_opy_()
    def event_key(self):
        pass
    def stop(self, time=None, duration=None, result=None):
        self.bstack1ll1l1l1lll_opy_ = time if time else bstack1l1l1lll_opy_()
        self.duration = duration if duration else bstack1111ll1ll1l_opy_(self.started_at, self.bstack1ll1l1l1lll_opy_)
        if result:
            self.result = result
class bstack1l11l1ll_opy_(bstack1ll1llll_opy_):
    def __init__(self, hooks=[], bstack1l1lllll_opy_={}, *args, **kwargs):
        self.hooks = hooks
        self.bstack1l1lllll_opy_ = bstack1l1lllll_opy_
        super().__init__(*args, **kwargs, bstack11llll1ll1_opy_=bstack1ll1l_opy_ (u"ࠬࡺࡥࡴࡶࠪἎ"))
    @classmethod
    def bstack11111l11111_opy_(cls, scenario, feature, test, **kwargs):
        steps = []
        for step in scenario.steps:
            steps.append({
                bstack1ll1l_opy_ (u"࠭ࡩࡥࠩἏ"): id(step),
                bstack1ll1l_opy_ (u"ࠧࡵࡧࡻࡸࠬἐ"): step.name,
                bstack1ll1l_opy_ (u"ࠨ࡭ࡨࡽࡼࡵࡲࡥࠩἑ"): step.keyword,
            })
        return bstack1l11l1ll_opy_(
            **kwargs,
            meta={
                bstack1ll1l_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࠪἒ"): {
                    bstack1ll1l_opy_ (u"ࠪࡲࡦࡳࡥࠨἓ"): feature.name,
                    bstack1ll1l_opy_ (u"ࠫࡵࡧࡴࡩࠩἔ"): feature.filename,
                    bstack1ll1l_opy_ (u"ࠬࡪࡥࡴࡥࡵ࡭ࡵࡺࡩࡰࡰࠪἕ"): feature.description
                },
                bstack1ll1l_opy_ (u"࠭ࡳࡤࡧࡱࡥࡷ࡯࡯ࠨ἖"): {
                    bstack1ll1l_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ἗"): scenario.name
                },
                bstack1ll1l_opy_ (u"ࠨࡵࡷࡩࡵࡹࠧἘ"): steps,
                bstack1ll1l_opy_ (u"ࠩࡨࡼࡦࡳࡰ࡭ࡧࡶࠫἙ"): bstack11l11l11111_opy_(test)
            }
        )
    def bstack111111lll11_opy_(self):
        return {
            bstack1ll1l_opy_ (u"ࠪ࡬ࡴࡵ࡫ࡴࠩἚ"): self.hooks
        }
    def bstack111111lllll_opy_(self):
        if self.bstack1l1lllll_opy_:
            return {
                bstack1ll1l_opy_ (u"ࠫ࡮ࡴࡴࡦࡩࡵࡥࡹ࡯࡯࡯ࡵࠪἛ"): self.bstack1l1lllll_opy_
            }
        return {}
    def bstack111111ll1ll_opy_(self):
        return {
            **super().bstack111111ll1ll_opy_(),
            **self.bstack111111lll11_opy_()
        }
    def bstack11111l1111l_opy_(self):
        return {
            **super().bstack11111l1111l_opy_(),
            **self.bstack111111lllll_opy_()
        }
    def event_key(self):
        return bstack1ll1l_opy_ (u"ࠬࡺࡥࡴࡶࡢࡶࡺࡴࠧἜ")
class bstack1l1ll11l_opy_(bstack1ll1llll_opy_):
    def __init__(self, hook_type, *args,bstack1l1lllll_opy_={}, **kwargs):
        self.hook_type = hook_type
        self.bstack1l111llll11_opy_ = None
        self.bstack1l1lllll_opy_ = bstack1l1lllll_opy_
        super().__init__(*args, **kwargs, bstack11llll1ll1_opy_=bstack1ll1l_opy_ (u"࠭ࡨࡰࡱ࡮ࠫἝ"))
    def bstack1l1l11l1_opy_(self):
        return self.hook_type
    def bstack11111l11l11_opy_(self):
        return {
            bstack1ll1l_opy_ (u"ࠧࡩࡱࡲ࡯ࡤࡺࡹࡱࡧࠪ἞"): self.hook_type
        }
    def bstack111111ll1ll_opy_(self):
        return {
            **super().bstack111111ll1ll_opy_(),
            **self.bstack11111l11l11_opy_()
        }
    def bstack11111l1111l_opy_(self):
        return {
            **super().bstack11111l1111l_opy_(),
            bstack1ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡥࡲࡶࡰࡢ࡭ࡩ࠭἟"): self.bstack1l111llll11_opy_,
            **self.bstack11111l11l11_opy_()
        }
    def event_key(self):
        return bstack1ll1l_opy_ (u"ࠩ࡫ࡳࡴࡱ࡟ࡳࡷࡱࠫἠ")
    def bstack11ll1111_opy_(self, bstack1l111llll11_opy_):
        self.bstack1l111llll11_opy_ = bstack1l111llll11_opy_